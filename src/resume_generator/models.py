from django.db import models
from user_profiles.models import Profile


# Create your models here.
class Resume(models.Model):
    resume_title = models.CharField(max_length=70)
    resume_developer_role = models.CharField(max_length=120)
    resume_short_intro = models.TextField(max_length=200)
    skill_summary = models.TextField()
    resume_image = models.ImageField(upload_to="images", default="avatar7.png")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Education(models.Model):
    name_of_educational_qualification = models.CharField(max_length=70)
    name_of_the_institution = models.CharField(max_length=120)
    name_of_the_department = models.CharField(max_length=70)
    passing_year = models.CharField(max_length=4)
    grade = models.DecimalField(max_digits=3, decimal_places=2)
    profile = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)


class SkillDescription(models.Model):
    skill_description = models.CharField(max_length=255)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class ResumeProjects(models.Model):
    project_title = models.CharField(max_length=70)
    github_link = models.URLField(null=True, blank=True)
    technologies_used = models.CharField(max_length=255)
    project_summary = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Hobby(models.Model):
    name = models.CharField(max_length=20)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class References(models.Model):
    referrer = models.CharField(max_length=255)
    referrer_institution = models.CharField(max_length=255)
    referrer_job_title = models.CharField(max_length=255)
    referrer_phn = models.CharField(max_length=15)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
