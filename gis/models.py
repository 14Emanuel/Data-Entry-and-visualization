from django.db import models

class NavigationEntry(models.Model):
    sno = models.IntegerField()
    unique_id = models.CharField(max_length=10)
    coordinates = models.CharField(max_length=50)
    gis = models.CharField(max_length=50)
    plus_code = models.CharField(max_length=100)
    nearby_railway_address = models.CharField(max_length=50)  # Changed variable name
    nearby_railway_station = models.CharField(max_length=50)  # New column for Nearby Railway Station
    photos = models.BinaryField(null=True)
    videos = models.BinaryField(null=True)
    type_of_item = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    verified_scrap_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('NaN', 'NaN'),
    )
    verified_scrap = models.CharField(max_length=3, choices=verified_scrap_choices)

    pending_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('NaN', 'NaN'),
    )
    pending_department = models.CharField(max_length=3, choices=pending_choices)

    lot_no_engineering = models.CharField(max_length=20)
    lot_no_stores = models.CharField(max_length=20)

    auction_date_given_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('NaN', 'NaN'),
    )
    auction_date_given = models.CharField(max_length=3, choices=auction_date_given_choices)

    fdp_date = models.CharField(max_length=8)  # Format: ddmmyyyy

    phone_no = models.CharField(max_length=15)  # Update the max length according to your needs
    custodian = models.CharField(max_length=50)  # Update the max length according to your needs
    approx_weight = models.CharField(max_length=10)
    approx_rate = models.CharField(max_length=10)

    def __str__(self):
        return self.unique_id

    class Meta:
        db_table = 'dummy'  # Set the collection name to 'dummy'
