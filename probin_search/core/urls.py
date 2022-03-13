from django.urls import path
from .views import PersonListView,PersonListTable, PersonDetailView, SearchResultView

app_name = 'person'
urlpatterns = [
    path('', PersonListView.as_view(), name='index'),
    path('list/', PersonListTable.as_view(), name='list-table'),
    

    path("<int:pk>/", PersonDetailView.as_view(), name='person-detail'),
    path("search/", SearchResultView.as_view(), name='search'),
]
