from django.db import models

from users.models import User

class Account(models.Model):
    name    = models.CharField(max_length=200)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField(max_digits=30, decimal_places=2)

    class Meta:
        db_table = 'accounts'
    