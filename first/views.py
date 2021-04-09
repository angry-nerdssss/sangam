from .models import Organisation, Invitation, Hosting, Feedback_after_event,Feedback
import math
from .models import Organisation, Invitation
from django.shortcuts import render, redirect, get_object_or_404, reverse


# organisation name
# category
# organisation email
# contact no
# description
# motto
# location
# certifiacte
# two conditions are required 1)validation of email, 2)verification by admin


def index(request):
    return render(request, "index.html")

# this function is to set register conditions and functionality
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        contact = request.POST['contact']
        description = request.POST['description']
        password = request.POST['password']
        form = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            organisation_name = newform.organisation_name
            newform.slug = slugify(organisation_name)
            newform.save()
            form.save_m2m()
            organisation = Organisation.objects.get(
                organisation_name=organisation_name)
            organisation.email = email
            organisation.password = password
            organisation.description = description
            organisation.contact = contact
            organisation.save()
            user = User.objects.create_user(
                username=organisation_name, email=email, password=password)
            # by writing this only we are hitting the database to store the information
            user.save()
            return redirect('login')
        else:
            print("5")
        form = OrganisationForm()
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)
    else:
        form = OrganisationForm()

        context = {
            'form': form,
        }
        return render(request, 'register.html', context)
