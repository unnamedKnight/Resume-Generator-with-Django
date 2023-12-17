from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Profile(models.Model):
    GENDER = (
        ("m", "male"),
        ("f", "female"),
    )

    full_name = models.CharField(max_length=70)
    developer_role = models.CharField(max_length=70)
    short_intro = models.TextField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(editable=False)
    address = models.CharField(max_length=70)
    profile_image = models.ImageField(
        upload_to="images/", default="avatar7.png"
    )

    fathers_name = models.CharField(max_length=70, blank=True, null=True)
    mothers_name = models.CharField(max_length=70, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    gender = models.CharField(
        max_length=15, choices=GENDER, default=GENDER[0][1]
    )

    religion = models.CharField(max_length=15, blank=True, null=True)
    nationality = models.CharField(max_length=15, blank=True, null=True)
    martial_status = models.BooleanField(default=False, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
