from django.db import models

# Create your models here.
class Cutomer(models.Model):
      customer_name = models.CharField(max_length =50)
      gender = models.CharField(max_length=50)
      email = models.CharField (max_length=50)
      customer_phonenumber = models.CharField (max_length=50)
      customer_address = models.CharField (max_length=500)
      customer_password = models.CharField (max_length=150)
      customer_image = models.ImageField(upload_to='customer/')

      class Meta:
            db_table = 'customer_tb'

