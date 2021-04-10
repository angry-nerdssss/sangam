  
from django.contrib import admin

from .models import Organisation,Fund,Invitation,Don,Feedback,Feedback_after_event,Hosting
# Register your models here.
admin.site.register(Organisation)
admin.site.register(Fund)
admin.site.registeron(Invitation)
admin.site.register(Don)
admin.site.register(Feedback)
admin.site.register(Feedback_after_event)
admin.site.register(Hosting)