from django.db import models

# Create your models here.
class Updatedata(models.Model):
    update_name = models.CharField(max_length = 100)
    update_date = models.DateTimeField(default = None)
    update_type = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.update_name}"


class Prakasam(models.Model):
    prakasam_view = models.ForeignKey(Updatedata, on_delete = models.CASCADE, related_name="prakasam_data", null=True)
    prakasam_matter = models.TextField(blank=True, null=True)
    prakasam_image = models.ImageField(upload_to='images', blank=True)
    prakasam_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.prakasam_view}"

class Gandhi(models.Model):
    gandhi_view = models.ForeignKey(Updatedata, on_delete = models.CASCADE, related_name="gandhi_data")
    gandhi_matter = models.TextField(blank=True, null=True)
    gandhi_image = models.ImageField(upload_to='images', blank=True)
    gandhi_date = models.DateTimeField(default = None, null=True)

    def __str__(self):
        return f"{self.gandhi_view}"

class Polytechnic(models.Model):
    polytechnic_view = models.ForeignKey(Updatedata, on_delete = models.CASCADE, related_name="polytechnic_data")
    polytechnic_matter = models.TextField(blank=True, null=True)
    polytechnic_image = models.ImageField(upload_to='images', blank=True)
    polytechnic_date = models.DateTimeField(default = None)

    def __str__(self):
        return f"{self.polytechnic_view}"
