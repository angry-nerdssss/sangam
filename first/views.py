from .models import Organisation, Invitation, Hosting, Feedback_after_event,Feedback
import math


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