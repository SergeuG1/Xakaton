from django.contrib import admin
from users.models import *



admin.site.register(User)
admin.site.register(UserProfiles)
admin.site.register(SavedCoord)
admin.site.register(Roles)
admin.site.register(Regions)
admin.site.register(ProblemCategories)
admin.site.register(News)
admin.site.register(ExecutiveAuthority)
admin.site.register(MailingQueue)
admin.site.register(Applications)
admin.site.register(ApplicationStatus)
admin.site.register(AdminApplications)

