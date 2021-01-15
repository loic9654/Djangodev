from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    folderName = models.CharField(max_length=200)
    

class Observation   (models.Model):
    client = models.ForeignKey(Project , on_delete=models.CASCADE)
    last_update = models.DateTimeField('last update')
    text = models.CharField(max_length=500)
    

    def __str__(self):
        return self.text