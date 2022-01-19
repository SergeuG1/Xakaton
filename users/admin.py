from django.contrib import admin
from users.models import *


@admin.register(Applications)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("problem_desc","user", "status","get_title")
    search_fields  = ("problem_desc","user__login","status__title")

    list_filter = ("status",)
    def get_title(self, obj):
        return obj.status.title
    get_title.short_description = 'status_code'
    get_title.admin_order_field = 'status__title'


admin.site.register(User)
admin.site.register(UserProfiles)
admin.site.register(SavedCoord)
admin.site.register(Roles)
admin.site.register(Regions)
admin.site.register(ProblemCategories)
admin.site.register(News)
admin.site.register(ExecutiveAuthority)
admin.site.register(MailingQueue)
# admin.site.register(Applications)
admin.site.register(ApplicationStatus)
admin.site.register(AdminApplications)

