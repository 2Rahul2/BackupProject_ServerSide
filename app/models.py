from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
# Create your models here.

User = get_user_model()
class FolderFiles(models.Model):
    name = models.CharField(max_length=500)
    file = models.BinaryField()
    subBranchId = models.IntegerField()

    def __str__(self):
        return str(self.id)

class SubFolder(models.Model):
    name = models.CharField(max_length=500)
    mainBranchId = models.IntegerField()
    SecondaryBranchId = models.IntegerField(null=True)
    subFolder = models.ManyToManyField('self',null=True , symmetrical=False)
    files = models.ManyToManyField(FolderFiles)

    def __str__(self):
        return self.name
class MainBranch(models.Model):
    user = models.ForeignKey(User  , blank=True ,null=True ,on_delete=models.SET_NULL)
    name = models.CharField(max_length=500)
    subFolder = models.ManyToManyField(SubFolder ,null=True ,blank=True)
    files = models.ManyToManyField(FolderFiles ,null=True ,blank=True)

    def __str__(self):
        return str(self.id)


    