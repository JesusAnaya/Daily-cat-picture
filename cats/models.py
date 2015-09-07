from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.email
