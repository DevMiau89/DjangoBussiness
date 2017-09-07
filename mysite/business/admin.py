from django.contrib import admin

# Register your models here.
from .models import Post, Portfolio, Employee


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']
    list_editable = ['title']
    search_fields = ['title', "content"]

    class Meta:
        model = Post


class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'industry', 'country', 'updated', 'timestamp']
    search_fields = ['title', 'industry']
    list_editable = ['title']
    list_filter = ['industry', 'updated', 'timestamp']
    list_display_links = ['industry']

    class Meta:
        model = Portfolio


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'department', 'email']
    search_fields = ['full_name', 'department', 'job_title']
    list_filter = ['full_name', 'department', 'job_title']
    list_display_links = ['job_title']

    class Meta:
        model = Employee


admin.site.register(Post, PostModelAdmin)
admin.site.register(Portfolio, PortfolioModelAdmin)
admin.site.register(Employee, EmployeeModelAdmin)
