from django.db import models

# Create your models here.
class productMainModel(models.Model):
    choice = (
    (('10'), '10'), ('20', '20'),('30', '30')
    )
   
    Qualitychoice=(
        ("high",'high'),
        ("low",'low'),
        ("meduim",'medium'),
    )
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    Price=models.IntegerField()
    unique_code=models.IntegerField(unique =True)
    Size = models.CharField(max_length=20,choices=choice)
    Quality = models.CharField(max_length=20,choices=Qualitychoice)
    
    
    
class productColourModel(models.Model):
    colorchoice=(
        ("red","red"),
        ("blue","blue"),
        ("green","green"),
        ("black","black"),
    )
    Product =models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Colour = models.CharField(max_length=20,choices=colorchoice)


class productImageModel(models.Model):
    Product = models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='productimage',null=True,blank=True)


