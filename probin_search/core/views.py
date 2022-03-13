from .models import Person
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
import re

# Provide list
class PersonListTable(ListView):
    model = Person
    template_name = 'core/list_table.html'
    

# Create your views here.
class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class SearchResultView(ListView):
    model = Person
    template_name = 'person/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        value = query.strip()
        print(value);
        
        object_list = Person.objects.filter(
            Q(name__icontains=value) | Q(father_name__icontains=value) |
            Q(nid_number__icontains=value) | Q(age__icontains=value) |
            Q(current_address__icontains=value) | Q(permanent_address__icontains=value) |
            Q(mobile_number__icontains=value) | Q(occupassion__icontains=value)
        )

        return object_list
