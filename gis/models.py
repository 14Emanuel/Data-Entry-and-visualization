from django.db import models

class NavigationEntry(models.Model):
    sno = models.IntegerField()
    unique_id = models.CharField(max_length=10)
    coordinates = models.CharField(max_length=50)
    gis = models.CharField(max_length=50)
    plus_code = models.CharField(max_length=100)
    nearby_location = models.CharField(max_length=50)  # Update the max length according to your needs
    photos = models.BinaryField(null=True)  # Add the photos field with BinaryField
    videos = models.BinaryField(null=True)  # Add the videos field with BinaryField
    type_of_item = models.CharField(max_length=50)  # Update the max length according to your needs
    status = models.IntegerField()
    

    def __str__(self):
        return self.unique_id

    class Meta:
        db_table = 'dummy'  # Set the collection name to 'dummy'
