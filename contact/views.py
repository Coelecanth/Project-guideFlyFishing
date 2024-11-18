from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()

            messages.info(
                request,
                "Thank You! We'll be in touch with you soon!"
            )
            return redirect(reverse("home"))

    template = "contact/contact.html"
    context = {
        "contact_form": contact_form,
    }
    return render(request, template, context)

