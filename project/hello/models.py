from django.db import models


class Company(models.Model):

    company_id = models.IntegerField(verbose_name="Company_ID")
    name = models.CharField(max_length=200, verbose_name="Company_name")
    location = models.CharField(max_length=1024, verbose_name="Location")

    def __str__(self):
        return self.name


class Products(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_id = models.IntegerField(verbose_name="Product_ID")
    name = models.CharField(max_length=200, verbose_name="Product_Name")

    def __str__(self):
        return self.name
