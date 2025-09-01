from django.contrib import admin
from .models import *

class OrganizationAdmin(admin.ModelAdmin):
    list_display=['id','name','address','created_at','updated_at']

class BatchAdmin(admin.ModelAdmin):
    list_display=['id','name','start_date','end_date','total_students','active','organization','created_at','updated_at']

class FeedbackAdmin(admin.ModelAdmin):
    list_display=['id','kbefore','kafter','communication','content','handson','interaction','speed','rating','feedback','suggestions','batch','submitted_at']


admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Feedback,FeedbackAdmin)