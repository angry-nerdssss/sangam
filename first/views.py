
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

