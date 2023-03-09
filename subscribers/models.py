from django.db import models




class Subscribers(models.Model):

    email = models.CharField(max_length= 100, blank=False, null=False, help_text="Email Adress")
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text="First and Last Name")

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"