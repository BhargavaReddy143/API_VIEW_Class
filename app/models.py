from django.db import models

# Create your models here.


class Product_Category(models.Model):
    Id=models.IntegerField(primary_key=True)
    PCname=models.CharField(max_length=50)


    def __str__(self):
        return self.PCname

class Product(models.Model):
    PCname=models.ForeignKey(Product_Category, on_delete=models.CASCADE) 
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=50)
    Pdate=models.DateField()


    def __str__(self):
        return self.Pname
