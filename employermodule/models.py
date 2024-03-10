from django.db import models

class BusDetails(models.Model):
    bus_name = models.CharField(max_length=255)
    ticket_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Specify decimal places

    BUS_TYPES = [
        ('sleeper', 'Sleeper'),
        ('semisleeper', 'Semi-sleeper'),
        ('sitting', 'Sitting')
    ]
    bus_type = models.CharField(max_length=20, choices=BUS_TYPES)

    # Assuming noofseats should be an integer, use IntegerField
    noofseats = models.IntegerField()  # Change to IntegerField

    pickup = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)


    provisions = models.CharField(max_length=255)

    def __str__(self):
        return self.bus_name
