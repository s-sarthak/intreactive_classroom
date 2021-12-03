from django.contrib import admin
from .models import Profile, TimeTable, Assignment, Querie, AssignmentSubmission
from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.unregister(Site)
# Register your models here.


class TimeTableAdmin(admin.ModelAdmin):
	list_display= ('id', 'image')
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
class AssignmentAdmin(admin.ModelAdmin):
	list_display= ('code', 'class_sec','topic','deadline')
class AssignmentSubmissionAdmin(admin.ModelAdmin):
	list_display= ('roll_no', 'name','code','class_sec', 'timestamp')
	list_filter = ('code', 'class_sec')
class QuerieAdmin(admin.ModelAdmin):
	list_display= ('name','email','timestamp')
class ProfileAdmin(admin.ModelAdmin):
	list_display= ('name','email','dob', 'phone_no')
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
admin.site.register(Profile,ProfileAdmin)
admin.site.register(TimeTable,TimeTableAdmin)
admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(AssignmentSubmission,AssignmentSubmissionAdmin)
admin.site.register(Querie,QuerieAdmin)

