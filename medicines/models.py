from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=150)
    manufacture_company = models.CharField(max_length=150)
    expiry_date = models.DateField()
    year_of_manufacture = models.IntegerField()
    composition = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    # compare_price = models.CharField(max_length=30)


    @classmethod
    def check_medicine(cls, name, manufacture_company, year_of_manufacture):
        return cls.objects.filter(name=name, manufacture_company=manufacture_company, year_of_manufacture=year_of_manufacture).exists()

    