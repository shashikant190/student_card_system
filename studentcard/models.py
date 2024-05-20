from django.db import models

# Create your models here.


class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# For utils Barcode

class StudentCard(models.Model):
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
#     barcode = models.ImageField(upload_to='barcodes/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'