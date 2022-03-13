from django.db import models
from django_resized import ResizedImageField


class Person(models.Model):
    
    MOBILE_BANKING = (
        ('bkash', 'বিকাশ'),
        ('nagad', 'নগদ'),
    )
    
    
    form_number = models.CharField(max_length=8, null=True, blank=True)
    name = models.CharField(max_length=89)
    house_number = models.CharField(max_length=21, null=True, blank=True)
    birth_date = models.DateField(auto_now_add=False, null=True, blank=True)
    age = models.CharField(max_length=89)
    nid_number = models.CharField(max_length=89)
    mobile_number = models.CharField(max_length=89)
    mobile_banking = models.CharField(max_length=89, choices=MOBILE_BANKING ,null=True, blank=True)
    
    father_name = models.CharField(max_length=89, blank=True, null=True) 
    current_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    birth_place = models.CharField(max_length=89, blank=True, null=True, default='এখন ও যুক্ত করা হয় নাই')
    
    occupassion = models.CharField(max_length=89, blank=True, null=True)
    illness = models.CharField(max_length=89, blank=True, null=True)
    religion = models.CharField(max_length=55, blank=True, null=True)
    child_count = models.CharField(max_length=89, blank=True, null=True)
    living = models.CharField(max_length=144, blank=True, null=True)
    image = ResizedImageField(size=[640, 480], upload_to = 'old/resized/', blank=True, null=True)

    def __str__(self):
        return self.name

