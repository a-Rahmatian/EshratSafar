from django.db import models

class company(models.Model):
    name=models.CharField(max_length=20)
    kind=models.CharField(max_length=8)
    reigstrationCode=models.IntegerField()



class travel(models.Model):
    origin=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    travelDate=models.DateField()
    travelTime=models.TimeField(null=True)
    travelKind=models.CharField(max_length=8)
    capacity=models.IntegerField()
    company=models.ForeignKey('company',related_name="company",on_delete=models.CASCADE)
    price=models.CharField(max_length=9,default="0")
    terminal=models.CharField(max_length=20,null=True)

class passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    nationalCode=models.CharField(max_length=10)
    gender=models.CharField(max_length=6)
    birthDate=models.DateField()


class ticket(models.Model):
    passenger=models.ForeignKey('passenger',related_name='passenger',on_delete=models.CASCADE)
    travel=models.ForeignKey("travel", related_name='travel', on_delete=models.CASCADE)

class supporter(models.Model):
    phoneNumber2=models.CharField(max_length=11)
    phoneNumber1=models.CharField(max_length=11,default="0")
    whatsapp=models.URLField(max_length=200,null=True)
    telegram=models.URLField(max_length=200,null=True)

class admin1(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    name=models.CharField(max_length=30)
    site=models.CharField(max_length=30)
    

class terminal(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    kind=models.CharField(max_length=40)

class city(models.Model):
    label=models.CharField(max_length=30)
    slug=models.CharField(max_length=30)
   



