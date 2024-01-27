from django.urls import path
from django.views.generic import TemplateView

from home.views import CreateContactView, ListContactView, UpdateContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('create/', CreateContactView.as_view(), name='create-contact'),
    path('list/', ListContactView.as_view(), name='list-contact'),
    path('<int:pk>/update/', UpdateContactView.as_view(), name='update-contact'),
]
