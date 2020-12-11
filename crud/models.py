from django.db import models


class Employee(models.Model):
 sr_no = models.IntegerField(default=1)
 first_name = models.CharField(max_length=60)
 last_name = models.CharField(max_length=60)
 email = models.EmailField(max_length=60)

