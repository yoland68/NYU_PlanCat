from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from basic.models import Class, Major, Course, FalbertUser

# Re-register UserAdmin
class ClassAdmin(admin.ModelAdmin):
    list_display = ("class_id",)
    search_fields = ['class_id']

    class Meta:
        verbose_name_plural = "classes"

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id",)
    search_fields = ['course_id']

class MajorAdmin(admin.ModelAdmin):
    list_display = ("major_id",)
    search_fields = ['major_id']

admin.site.register(Class, ClassAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(FalbertUser)
