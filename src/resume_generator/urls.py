from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #     resume views
    path("create-resume", views.create_resume, name="create_resume"),
    path("resume-detail/<id>", views.resume_detail_view, name="resume_detail_view"),
    path("resume-update/<id>", views.resume_update_view, name="resume_update_view"),
    path("resume-delete/<id>", views.resume_delete_view, name="resume_delete_view"),

    # resume template update view
    path("resume-template-update/<id>", views.resume_template_update_view,
         name="resume_template_update_view"),
    #     end of resume views
    # ------------------ educational details links ---------------- #

    path("add-educational-details", views.create_educational_detail,
         name="add_educational_details"),
    path("update-educational-detail/<id>",
         views.update_educational_detail, name="update_educational_detail"),
    path("delete-educational-detail/<id>",
         views.delete_educational_detail, name="delete_educational_detail"),

    # -------------- end of educational details links ------------- #

    # ---------------------- skill description --------------------- #

     # the following url takes a resume instance id
    path("create-skill-description/<id>",
         views.create_skill, name="create_skill"),
     # the following url takes a skill_description instance id
    path("update-skill-description/<id>",
         views.update_skill, name="update_skill"),
     # the following url takes a skill_description instance id
    path("delete-skill-description/<id>",
         views.delete_skill, name="delete_skill"),

    # ------------------ end of skill description ------------------ #
    # ----------------------- resume projects ---------------------- #

     # the following url takes a resume instance id
    path("create-resume-project/<id>",
         views.create_resume_project, name="create_resume_project"),
     # the following url takes a resume_project instance id
    path("update-resume-project/<id>",
         views.update_resume_project, name="update_resume_project"),
     # the following url takes a resume_project instance id
    path("delete-resume-project/<id>",
         views.delete_resume_project, name="delete_resume_project"),

    # ------------------- end of resume projects ------------------- #
    # ---------------------------- hobby --------------------------- #

     # the following url takes a resume instance id
    path("create-hobby/<id>",
         views.create_hobby, name="create_hobby"),
     # the following url takes a hobby instance id
    path("update-hobby/<id>",
         views.update_hobby, name="update_hobby"),
     # the following url takes a hobby instance id
    path("delete-hobby/<id>",
         views.delete_hobby, name="delete_hobby"),

    # ------------------------ end of hobby ------------------------ #
    # -------------------------- reference ------------------------- #

     # the following url takes a resume instance id
    path("create-reference/<id>",
         views.create_reference, name="create_reference"),
     # the following url takes a reference instance id
    path("update-reference/<id>",
         views.update_reference, name="update_reference"),
     # the following url takes a reference instance id
    path("delete-reference/<id>",
         views.delete_reference, name="delete_reference"),

    # ---------------------- end of reference ---------------------- #



]
