from django.db import models

# Create your models here.
class Andhra(models.Model):
    stno=models.IntegerField(primary_key=True)
class District(models.Model):
    dname=models.CharField(max_length=100)
    stno=models.ForeignKey(Andhra,on_delete=models.CASCADE)
    areas=models.CharField(max_length=100,unique=True)
class Mandal(models.Model):
    dname=models.ForeignKey(District,on_delete=models.CASCADE)

    


