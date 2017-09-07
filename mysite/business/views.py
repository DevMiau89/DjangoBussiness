from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
# Create your views here.
from .models import Post, Portfolio,Employee


def index(request):
    return render(request, "index.html", {})


def about(request):
    queryset_list = Employee.objects.all()
    paginator = Paginator(queryset_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "employee_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "about.html", context)


def services(request):
    return render(request, "services.html", {})


def portfolio(request):
    portfolio_list = Portfolio.objects.all().order_by('-timestamp')
    # paginator = Paginator(queryset_portfolio_list, 3)
    # page_request_var = 'page'
    # page = request.GET.get(page_request_var)
    #
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     queryset = paginator.page(paginator.num_pages)

    context = {
        "portfolio_list": portfolio_list
        # "page_request_var": page_request_var,
    }
    return render(request, "portfolio.html", context)


def portfolio_detail(request, id=None):
    instance = get_object_or_404(Portfolio, id=id)
    context = {
        "instance": instance
    }
    return render(request, "portfolio_detail.html", context)


#Blog Handling
def blog(request):
    queryset_list = Post.objects.all() #.order_by('-timestamp')
    paginator = Paginator(queryset_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "post_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "blog.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance
    }

    return render(request, "post_detail.html", context)


def faq(request):
    return render(request, "faq.html", {})


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data["name"]
            form_email = form.cleaned_data["email"]
            form_phone = form.cleaned_data["phone"]
            form_message = form.cleaned_data["message"]

            #email send
            subject = "Site contact form"
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "lizinczyk.karolina@gmail.com"]
            contact_message = """
            Message from : {0}
            Message content: {1}
            Email : {2}
            Phone : {3}
            """.format(form_name, form_message, form_email, form_phone)

            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=False)

            messages.success(request, "Thank you for the message. We will get back to you shortly.")
            return render(request, "contact.html", {
                "form": form, "name": form_name, "email": form_email, "phone":  form_phone, "message": form_message,
            })
    return render(request, "contact.html", {})



