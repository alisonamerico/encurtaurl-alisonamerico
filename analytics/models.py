from django.db import models

from shortener.models import encurtaURL


class ClickEventManager(models.Manager):
    def create_event(self, shortInstance):
        if isinstance(shortInstance, encurtaURL):
            obj, created = self.get_or_create(curtUrl=shortInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    #clickEvent
    curtUrl     = models.OneToOneField(encurtaURL)
    count       = models.IntegerField(default=0)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
