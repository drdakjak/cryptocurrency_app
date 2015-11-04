from django.db import models
from django.utils import timezone

class Pubticker(models.Model):
    pair_id = models.CharField(max_length=20);
    id = models.AutoField(primary_key=True);
    import_date = models.DateTimeField(default=timezone.now);
    mid = models.DecimalField(max_digits=30, decimal_places=10);
    bid = models.DecimalField(max_digits=30, decimal_places=10);
    ask = models.DecimalField(max_digits=30, decimal_places=10);
    last_price = models.DecimalField(max_digits=30, decimal_places=10);
    low = models.DecimalField(max_digits=30, decimal_places=10);
    high = models.DecimalField(max_digits=30, decimal_places=10);
    volume = models.DecimalField(max_digits=30, decimal_places=10);
    timestamp = models.DecimalField(max_digits=30, decimal_places=10);
    
    
class Trade(models.Model):
    id = models.AutoField(primary_key=True);
    pubticker = models.ForeignKey(Pubticker);
    close_price = models.DecimalField(max_digits=30, decimal_places=10);
    close_return = models.DecimalField(max_digits=30, decimal_places=10);
    