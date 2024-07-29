from django.db import models
from easymde.fields import EasyMDEField


class Markdown(models.Model):
    title = models.CharField(max_length=32)
    content = EasyMDEField()
