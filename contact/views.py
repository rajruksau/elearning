from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):

    template_name_1 = 'contact/contact.html'
    template_name_2 = 'contact/success.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name_2)
            
    form = ContactForm()
    context = {'form': form}
    return render(request, template_name_1, context)