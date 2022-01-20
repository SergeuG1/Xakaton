from django.contrib import admin
from users.models import *
from django_admin_geomap import ModelAdmin
from django.core.mail import send_mail
from django.conf import settings




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
        data = queryset.all()
        email_list = []
        for x in data:
            email_list.append(x.email)
        
        send_mail(
            subject='A cool subject',
            message='A stunning message',
            from_email=settings.EMAIL_HOST_USER,
            # recipient_list=["Otfonarua@gmail.com",]) 
            recipient_list=[x.email,]) 



admin.site.register(AdminApplications, AdminApplicationsEmail)



admin.site.register(Applications, Admin)
admin.site.register(User)
admin.site.register(UserProfiles)
admin.site.register(SavedCoord)
admin.site.register(Roles)
admin.site.register(Regions)
admin.site.register(ProblemCategories)
admin.site.register(News)
admin.site.register(ExecutiveAuthority)
admin.site.register(MailingQueue)
admin.site.register(ApplicationStatus)

