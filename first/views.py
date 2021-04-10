from .models import Organisation, Invitation, Hosting, Feedback_after_event,Feedback
import math
from django.contrib import messages
from django.contrib.auth.models import User, auth

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