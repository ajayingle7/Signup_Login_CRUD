from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mno = PhoneNumberField()


    def __str__(self):
        return f'{self.pid}--{self.name}--{self.email}--{self.mno}'

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.profile}--{self.pname}--{self.status}'


