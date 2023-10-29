from django.db import models

class Crypto_Price(models.Model):
    symbol = models.CharField(max_length=10, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

