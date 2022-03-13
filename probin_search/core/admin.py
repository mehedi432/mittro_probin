from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'father_name', 'current_address','permanent_address', 'nid_number', 'occupassion', 'illness', 'religion', 'child_count', 'living', 'mobile_number']
    search_fields = ('name', 'age', 'father_name', 'current_address','permanent_address', 'nid_number', 'occupassion', 'illness', 'religion', 'child_count', 'living', 'mobile_number')
