from django.views.generic import FormView, ListView, UpdateView
from django.urls import reverse_lazy
from home.forms import ContactForm, Contact


class ListContactView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'home/list.html'
    ordering = '-created_time'


class CreateContactView(FormView):
    form_class = ContactForm
    template_name = 'home/create-update.html'
    success_url = reverse_lazy('home:list-contact')

    def form_valid(self, form):
        form.save()
        return super(CreateContactView, self).form_valid(form)


class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/create-update.html'
    success_url = reverse_lazy('home:list-contact')

    def form_valid(self, form):
        form.save()
        return super(UpdateContactView, self).form_valid(form)
