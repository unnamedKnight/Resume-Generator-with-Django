from django.contrib import admin

# Register your models here.
from .models import Resume, Education, SkillDescription, ResumeProjects, Hobby, References

admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(SkillDescription)
admin.site.register(ResumeProjects)
admin.site.register(Hobby)
admin.site.register(References)
