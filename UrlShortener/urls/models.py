from django.db import models

# Create your models here.


class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    url = models.URLField()
    url_code = models.CharField(max_length = 10)
