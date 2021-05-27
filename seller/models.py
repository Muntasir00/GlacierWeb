from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='seller', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name