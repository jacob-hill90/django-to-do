from django.db import models

class item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField



    