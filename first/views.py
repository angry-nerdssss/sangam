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
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from taggit.models import Tag
from datetime import datetime, timedelta
from .forms import OrganisationForm

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
            organisation=Organisation.objects.get(organisation_name=organisation_name)
            organisation.email=email
            organisation.password=password
            organisation.description=description
            organisation.contact=contact
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


# this function is to set login conditions and functionality
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # by writing this we are checking whether the entered username and password are of the same user or not
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("1")
            return redirect('/')

        else:
            print("2")
            return render(request, 'login.html')
    else:
        print("3")
        return render(request, 'login.html')

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


def search(request):
    if request.method == 'POST':
        searched_query = request.POST['search_name']
        strings = subString(searched_query, len(searched_query))
        queryset1 = Organisation.objects.none()
        for string in strings:
            queryset1 |= Organisation.objects.filter(city__icontains=string)
            queryset1 |= Organisation.objects.filter(
                organisation_name__icontains=string)

        strings = []
        searched_type = request.POST['search_type']
        queryset1 &= Organisation.objects.filter(
            category__icontains=searched_type)
        recommended_organisation = reversed(queryset1)
        ctx = {
            'organisation': recommended_organisation,
        }
        return render(request, 'search.html', ctx)

    else:
        organisation = Organisation.objects.all()
        ctx = {'organisation': organisation}
        return render(request, 'search.html', ctx)


@login_required(login_url='login')
def profile(request, slug):
    organisation = get_object_or_404(Organisation, slug=slug)
    reciever = User.objects.get(username=organisation.organisation_name)
    sender = User.objects.get(username=request.user.username)
    feedbacks=Feedback_after_event.objects.filter(feedback_for=organisation)
    case = 0
    host_allow = 0
    invitation1 = Invitation.objects.filter(
        sender=sender).filter(reciever=reciever)
    invitation2 = Invitation.objects.filter(
        sender=reciever).filter(reciever=sender)
    if invitation1.exists():
        invitation = invitation1[0]
        # invitation=Invitation.objects.get(sender=sender,reciever=reciever)
        if invitation.accepted_or_not is True:
            case = 1  # is organisation ne accept kar liya hai inv
        else:
            case = 2  # abhi accept nhi kiya hai

    elif invitation2.exists():
        invitation = invitation2[0]
        if invitation.accepted_or_not is True:
            case = 3  # humne accept kar li hai accept kar liya hai inv
        else:
            case = 4  # humne accept nhi ki hai
    # invitation_case=1,2,3,4
    if case == 1 or case == 3:
        host_allow = 1
    print(case)
    ctx = {
        'org': organisation,
        'case': case,
        'host_allow': host_allow,
        'feedbacks':feedbacks,
    }
    return render(request, 'profile.html', ctx)


@login_required(login_url='login')
def profile2(request, id):
    user = get_object_or_404(User, pk=id)
    organisation = get_object_or_404(
        Organisation, organisation_name=user.username)
    reciever = User.objects.get(username=organisation.organisation_name)
    sender = User.objects.get(username=request.user.username)
    case = 0
    host_allow = 0
    invitation1 = Invitation.objects.filter(
        sender=sender).filter(reciever=reciever)
    invitation2 = Invitation.objects.filter(
        sender=reciever).filter(reciever=sender)
    if invitation1.exists():
        invitation = invitation1[0]
        # invitation=Invitation.objects.get(sender=sender,reciever=reciever)
        if invitation.accepted_or_not is True:
            case = 1  # is organisation ne accept kar liya hai inv
        else:
            case = 2  # abhi accept nhi kiya hai

    elif invitation2.exists():
        invitation = invitation2[0]
        if invitation.accepted_or_not is True:
            case = 3  # humne accept kar li hai accept kar liya hai inv
        else:
            case = 4  # humne accept nhi ki hai
    # invitation_case=1,2,3,4
    if case == 1 or case == 3:
        host_allow = 1
    print(case)
    ctx = {
        'org': organisation,
        'case': case,
        'host_allow': host_allow,
    }
    return render(request, 'profile.html', ctx)


def fundraise(request):
    return render(request, 'fundraiser.html')


def monthly_donation(request):
    return render(request, 'monthly_donation.html')


@login_required(login_url='login')
def send_invitation(request, slug):
    organisation = get_object_or_404(Organisation, slug=slug)
    reciever = User.objects.get(username=organisation.organisation_name)
    sender = User.objects.get(username=request.user.username)
    invitation1 = Invitation.objects.filter(
        sender=sender).filter(reciever=reciever)
    invitation2 = Invitation.objects.filter(
        sender=reciever).filter(reciever=sender)
    if invitation1.exists():
        return redirect('profile', slug)
    if invitation2.exists():
        invitation = invitation2[0]
        print("shi")
        invitation.accepted_or_not = True
        invitation.save()
        return redirect('profile', slug)
    invitation = Invitation.objects.create(
        sender=sender, reciever=reciever, accepted_or_not=False)
    invitation.save()
    return redirect('profile', slug)


@login_required(login_url='login')
def notification(request):
    notifications1 = Invitation.objects.filter(
        reciever=request.user).filter(accepted_or_not=False)
    notifications2 = Hosting.objects.filter(sender=request.user)
    notifications3 = Hosting.objects.filter(reciever=request.user)
    notifications2 = notifications2.filter(feedback_done=False)
    deadline = datetime.now().date()-timedelta(1)
    notifications2 = notifications2.filter(meeting_date=deadline)
    print(deadline)
    print("\n")
    print()
    notifications3 = notifications3.filter(feedback_done=False)
    notifications3 = notifications3.filter(meeting_date=deadline)
    print(notifications3.count())
    print(notifications2.count())
    ctx = {
        'notifications1': notifications1,
        'notifications2': notifications2,
        'notifications3': notifications3,
    }
    return render(request, 'notification.html', ctx)


def feedback_after_event(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=id)
        organisation = Organisation.objects.get(
            organisation_name=user.username)
        how_day = request.POST['how_day']
        how_other = request.POST['how_other']
        rate = request.POST['rate']
        hosting1 = Hosting.objects.filter(
            sender=user).filter(reciever=request.user)
        hosting2 = Hosting.objects.filter(
            sender=request.user).filter(reciever=user)
        our_organisation=get_object_or_404(Organisation,organisation_name=request.user.username)
        if hosting1.count() == 1:
            hosting = hosting1[0]
            hosting.feedback_done = True
            hosting.save()
        else:
            hosting = hosting2[0]
            hosting.feedback_done = True
            hosting.save()
        feedback = Feedback_after_event.objects.create(feedback_by=our_organisation,
            feedback_for=organisation, how_day=how_day, how_other=how_other, rate=rate)
        feedback.save()
        return redirect('notification')
    else:
        user = get_object_or_404(User, pk=id)
        ctx = {
            'feedback_for': user,
        }
        return render(request, 'feedback_after_event.html', ctx)


@login_required(login_url='login')
def hosting_event(request, slug):
    if request.method == 'POST':
        organisation = get_object_or_404(Organisation, slug=slug)
        reciever = User.objects.get(username=organisation.organisation_name)
        sender = User.objects.get(username=request.user.username)
        date = request.POST['date']
        venue = request.POST['venue']
        hosting = Hosting.objects.create(
            sender=sender, reciever=reciever, meeting_date=date, venue=venue)
        hosting.save()
        return redirect('profile', slug)
    else:
        organisation = get_object_or_404(Organisation, slug=slug)
        reciever = User.objects.get(username=organisation.organisation_name)
        sender = User.objects.get(username=request.user.username)
        ctx = {
            'sender_name': sender.username,
            'reciever_name': reciever.username,
            'slug': slug,
        }
        return render(request, 'hosting_page.html', ctx)


# this function is to take feedback


def feedback(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    feed = Feedback(name=name, email=email, subject=subject, message=message)
    # by writing this only we are hitting the database to store the information
    feed.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponseRedirect(reverse(request.path_info))

# this function is to show feedbacks from users to the admin


def show_feedback(request):
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'feedback.html', context)
