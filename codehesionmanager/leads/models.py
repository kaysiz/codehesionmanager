from django.db import models

class Lead(models.Model):
    # constants
    LEAD_ORIGIN = (
        ('Walkin', 'Walkin'),
        ('Phone', 'Phone'),
        ('Website', 'Website'),
    )

    LEAD_STATUS = [
        ('Pending', 'Pending'),
        ('Contacted', 'Contacted'),
    ]

    contact_name = models.CharField(max_length=150)
    contact_phone_number = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=100, unique=True)
    company_name = models.CharField(max_length=150, blank=True)
    origin = models.CharField(max_length=150, choices=LEAD_ORIGIN)
    status = models.CharField(max_length=150, choices=LEAD_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)