from django.contrib import admin
from django.shortcuts import render
from users.models import *
from django_admin_geomap import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from users.forms import SendEmailFrom



class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("create_date","problem_desc","user", "status","get_title")
    search_fields  = ("problem_desc","user__login","status__title")
    list_filter = ("status",)

    def get_title(self, obj):
        return obj.status.title

    
    get_title.short_description = 'status_code'
    get_title.admin_order_field = 'status__title'


class Admin(ModelAdmin, ApplicationAdmin):
    geomap_field_longitude = "longitude"
    geomap_field_latitude = "latitude"
    geomap_default_zoom = "3"
    geomap_item_zoom = "5"


    class Meta:
        proxy = True


class AdminApplicationsEmail(admin.ModelAdmin):
    actions = ["bulk_email"]
    def bulk_email(self, request, queryset):
        """ Make all posts published. """
        data = []
        for x in queryset:
            data.append(x.email)

        return render(request, 'admin/send_mail.html',context={'email': data, 'forms':SendEmailFrom})
      

class UsersAdmin(UserAdmin):
    pass


admin.site.register(AdminApplications, AdminApplicationsEmail)
admin.site.register(Applications, Admin)
admin.site.register(Users)
admin.site.register(UserProfiles)
admin.site.register(SavedCoord)
admin.site.register(Roles)
admin.site.register(Regions)
admin.site.register(ProblemCategories)
admin.site.register(News)
admin.site.register(ExecutiveAuthority)
admin.site.register(MailingQueue)
admin.site.register(ApplicationStatus)
admin.site.register(ApplicationsCategories)
admin.site.register(TokenBlocklist)

