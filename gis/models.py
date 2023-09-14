from djongo import models

class NavigationEntry(models.Model):
    mongo_id = models.ObjectIdField()
    unique_id = models.CharField(max_length=10)
    surveyor_id = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=50)
    nearby_station = models.CharField(max_length=50)
    scrap_location = models.CharField(max_length=100)
    scrap_category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    scrap_status = models.CharField(max_length=50)
    verified_scrap = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    pending_department = models.CharField(max_length=50)
    custodian = models.CharField(max_length=50)
    custodian_contact = models.CharField(max_length=15)
    approx_weight = models.CharField(max_length=10)
    approx_rate = models.CharField(max_length=10)
    remarks = models.TextField()

    def __str__(self):
        return str(self.mongo_id)

    class Meta:
        db_table = 'navigation_entry'

class Image(models.Model):
    navigation_entry = models.ForeignKey(NavigationEntry, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')  # Store images on disk

    def __str__(self):
        return f"Image for {self.navigation_entry.mongo_id}"
