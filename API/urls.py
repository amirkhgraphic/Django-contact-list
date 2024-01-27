from django.urls import path
from API.views import ListCreateContacts, SearchContacts, UpdateContact, DeleteContact

urlpatterns = [
    path('list/', ListCreateContacts.as_view(), name='list-contact'),
    path('search/', SearchContacts.as_view(), name='search-contact'),
    path('create/', ListCreateContacts.as_view(), name='create-contact'),
    path('update/', UpdateContact.as_view(), name='update-contact'),
    path('delete/<int:pk>', DeleteContact.as_view(), name='delete-contact'),
]
