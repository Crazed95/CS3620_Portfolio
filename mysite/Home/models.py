from django.db import models

# Create your models here.
class Hobbie(models.Model):

    def __str__(self):
        return self.hobbie_name

    hobbie_name = models.CharField(max_length=200)
    hobbie_desc = models.CharField(max_length=200)

class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name

    portfolio_name = models.CharField(max_length=200)
    port_desc = models.CharField(max_length=200)