
from distutils.command.upload import upload
from email.policy import default
from django.db import models
SHAPE_CHOICES = (
        ('ROUND', 'Round'),
        ('BOTTOM', 'Bottom'),
        ('SQUARE', 'Square'),
    )

CHOOSE_SIZE = (
('Extra Small', 'XS'),
('Small', 'S'),
('Medium', 'M'),
('Large', 'L'),
('Extra Large', 'XL'),
('Double Large', 'XXL'),
('Triple Large', 'XXXL'),
)

class User(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Product(models.Model):  
    product_name = models.CharField(max_length=250)
    shape = models.CharField(max_length=8,
                             choices=SHAPE_CHOICES,
                             default='',null=True)
    size = models.CharField(max_length=120, choices=CHOOSE_SIZE, null=True)
    image = models.ImageField(upload_to='images', default='')
    location = models.CharField(max_length=250)
    price =  models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product_name


class Recommendation(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



    
