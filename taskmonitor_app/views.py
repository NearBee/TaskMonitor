from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, UserRegistrationForm
from .models import User

# Create your views here.


def Register(request: HttpRequest) -> HttpResponse:
    """Create a user account.

    Args:
        request (HttpRequest): POST request to the register page.

    Returns:
        HttpResponse: Should return to a index page if successful
        if unsuccessful the user will be redirected back to the register.html page with a message
        as to why
    """

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        # two passwords required for confirmation
        password2 = request.POST["password_confirmation"]
        if form["password"].value() != password2:
            message = "Passwords don't match"  # TODO: Probably need to change this to be more ambiguous
            return render(
                request,
                "register.html",
                {"UserRegistrationForm": UserRegistrationForm, "message": message},
            )

        if form.is_valid():
            password = form["password"].value()
            email = form["email"].value()

            # display_name = form["display_name"].value()  || original method to createa a display name
            # Display name TEMPORARILY just using the beginning of the email
            # This is a temp(perhaps permanent) solution to a unique constraint with display_name
            display_name = email.rstrip("@")

            user = User.objects.create_user(display_name, password, email)
            login(request, user)
            return redirect("index")  # Needs to be made
        else:
            message = "Sorry something went wrong..."
            return render(
                request,
                "creation",
                {"UserRegistrationForm": UserRegistrationForm, "message": message},
            )

    else:
        return render(
            request, "register.html", {"UserRegistrationForm": UserRegistrationForm}
        )


def LoginView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form["email"].value()
            password = form["password"].value()
            user = User.object.get(email, password)  # type: ignore

            login(request, user)  # type: ignore
            return redirect("index")

        else:
            message = "Incorrect login credentials"
            return render(request, "")

    else:
        return render(request, "login.html", {"LoginForm": LoginForm})


@login_required(
    redirect_field_name="home/", login_url="login"
)  # Need to create the login html
def Index(request):
    pass


@login_required(login_url="login")
def CalendarView(request, username):
    # Calendar logic to be added here
    # You can also access the user who is logged in with request

    user = request.user
    context = {
        "username": username,
        "user": user,
    }

    return render(request, "calendar.html", context)
