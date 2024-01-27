from API.serializers import ContactSerializer, ListContactSerializer, Contact
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView


class SearchContacts(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ListContactSerializer

    def get_queryset(self):
        first_name = self.request.query_params.get('first-name', '')
        # last_name = self.request.query_params.get('last-name', '')
        # city = self.request.query_params.get('city', '')
        # country = self.request.query_params.get('country', '')

        return Contact.objects.filter(first_name__icontains=first_name)
                                      # last_name__icontains=last_name,
                                      # country__icontains=country,
                                      # city__icontains=city)


class ListCreateContacts(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ListContactSerializer


class UpdateContact(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DeleteContact(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
