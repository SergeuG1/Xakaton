from django.contrib import admin
from django.shortcuts import render
from users.models import *
from django_admin_geomap import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from users.forms import SendEmailFrom
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user","create_date","problem_desc", "status")
    search_fields  = ("problem_desc","user__login","status__title")
    list_filter = ("status",)
    change_list_template = 'admin/change_list.html'

    def changelist_view(self, request, extra_context=None):
        chart_data = (
            Applications.objects.annotate(date=TruncDay("create_date"))
            .values("date")
            .annotate(y=Count("id"))
        )

        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)


class Admin(ModelAdmin, ApplicationAdmin):
    geomap_field_longitude = "longitude"
    geomap_field_latitude = "latitude"
    geomap_default_zoom = "11"
    geomap_item_zoom = "5"
    geomap_default_longitude = "37.8022"
    geomap_default_latitude = "48.023"

    def changelist_view(self, request, extra_context=None):
        chart_data = (
            Applications.objects.annotate(date=TruncDay("create_date"))
            .values("date")
            .annotate(y=Count("id"))
        )

        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)
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





class RegionAdmin(admin.ModelAdmin):
    list_display = ("title","create_date")
    search_fields  = ("title",)

class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ("name","user","email","rate")
    search_fields  = ("name","user","phone_number")

class UserAdmin(admin.ModelAdmin):
    list_display = ("login","password","role")
    search_fields  = ("login",)

class ExecutiveAuthorityAdmin(admin.ModelAdmin):
    list_display = ("title","hash_tag","web_site_link")
    search_fields  = ("title","hash_tag",)



admin.site.register(AdminApplications, AdminApplicationsEmail)
admin.site.register(Applications, Admin)
admin.site.register(Users, UserAdmin)
admin.site.register(UserProfiles, UserProfilesAdmin)
admin.site.register(SavedCoord)
admin.site.register(Roles)
admin.site.register(Regions, RegionAdmin)
admin.site.register(ProblemCategories)
admin.site.register(News)
admin.site.register(ExecutiveAuthority, ExecutiveAuthorityAdmin)
admin.site.register(MailingQueue)
admin.site.register(ApplicationStatus)
admin.site.register(ApplicationsCategories)
admin.site.register(TokenBlocklist)

