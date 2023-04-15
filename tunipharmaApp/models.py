from datetime import date
from django.utils import timezone
from django.db import models

# Create your models here.

class Product(models.Model):
    label = models.CharField(max_length=20, default='')
    price = models.FloatField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='image/product_image',null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    expirationDate = models.DateField(default=date(2023,12,31))
    fabricationDate = models.DateField(default=timezone.now())
    class Meta:
        db_table ='product'
        
    def __str__(self):
        return f'name={self.name}, email={self.email}, phone ={self.phone},'

class Command(models.Model):
    commandNumber = models.PositiveIntegerField(default=1)
    clientNumber = models.PositiveIntegerField(default=00)
    status = models.TextField(default='')
    date_cmd = models.DateField(default=timezone.now())
    quality = models.PositiveSmallIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # OnetoMany relationship between product and command
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)  
    class Meta:
        # the table name in database 
        db_table ='command'
        #tuples in command table are orered by data_cmd 
        ordering = ['-date_cmd']
        # the name of the table in admin panel is command table(a name readable by humans)
        verbose_name = 'Command table'
        # the combinition of client, product and data_cmd must be unique
       # unique_together = [('client', 'product', 'date_cmd')]
    def __str__(self):
        return f'commandNumber={self.commandNumber}, date_cmd={self.date_cmd}, quantity ={self.quality},' 

class CommandDetails(models.Model):
    commandNumber = models.PositiveIntegerField(default=0)
    productNumber = models.PositiveIntegerField(default=0)
    productName = models.CharField(max_length=20, default='')
    quantity = models.PositiveIntegerField(default=1)
    unitPrice = models.FloatField(default=0.0)
    totalPrice = models.FloatField(default=0.0) 
    #onetoOne relationships between command and commandDetails:
    commad = models.OneToOneField(Command, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table ='command details'
        
class DeliveryInformation(models.Model):
    sendingNumber = models.PositiveIntegerField(default=1)
    Type = models.CharField(max_length=20, default='')
    Price = models.FloatField(default=0.0)
    destination = models.TextField(default='Rue, la ville , code de postal')
    #onetoOne relationships between command and DeliveryInformation:
    commad = models.OneToOneField(Command, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table ='delivery information'
   


