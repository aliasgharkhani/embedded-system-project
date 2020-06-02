from django.db import models


# Create your models here.
class ModuleLog(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    module_id = models.IntegerField()

    def __str__(self):
        return "{}-{}-{}-{}".format(self.module_id, self.date, self.temperature, self.humidity)
