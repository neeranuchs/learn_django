from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=400, blank = True)
    is_completed = models.BooleanField(default = False, blank = True)
    # created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = False)
    # updated_at = models.DateTimeField(auto_now = True, blank = True)
    # deleted_at = models.DateTimeField(default = False, auto_now = False, blank = True)

    # def __str__(self):
    #     return self.title