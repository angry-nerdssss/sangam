from .models import Organisation, Invitation, Hosting, Feedback_after_event,Feedback
import math
from .models import Organisation, Invitation
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.defaultfilters import slugify
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session


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






# this function is used to get user logged out


def logout(request):
    auth.logout(request)
    return redirect('/')


def subString(Str, n):
    strings = []
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            util_string = ""
            for k in range(i, j + 1):
                util_string = util_string+Str[k]

            x = len(Str)
            x = x//2
            if len(util_string) > x:
                strings.append(util_string)
    return strings

def organisation_page(request):
    organisation_name = request.POST['organisation_name']
    organisation = Organisation.objects.get(
        organisation_name=organisation_name)
    ctx = {
        'organisation': organistion,
    }
    return render(request, organisation_page.html, ctx)
