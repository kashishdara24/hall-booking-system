from django.db import models

class Booking(models.Model):
    applicant_name = models.CharField(max_length=100)
    hall_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    purpose = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.applicant_name} - {self.hall_name}"
