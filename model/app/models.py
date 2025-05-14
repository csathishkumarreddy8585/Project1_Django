from django.db import models

# Create your models here.


class Product_category(models.Model):
    pc_id=models.IntegerField(primary_key=True)
    pc_type=models.CharField(max_length=50)

    def __str__(self):
        return self.pc_id


class product(models.Model):
    pid=models.IntegerField(primary_key=50)
    productname=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    man_date=models.DateField()
    man_place=models.CharField(max_length=50)
    pc_id=models.ForeignKey(Product_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.productname