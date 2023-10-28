from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, JsonResponse

from .forms import user_registration_form
from .models import User

# Create your views here.


def creation(request: HttpRequest) -> HttpResponse:
    """Create a user account.

    Args:
        request (HttpRequest): POST request to the register page.

    Returns:
        HttpResponse: Should return to a index page if successful
        if unsuccessful the user will be redirected back to the register.html page with a message
        as to why
    """

    if request.method == "POST":
        form = user_registration_form(request.POST)

        # two passwords required for confirmation
        password2 = request.POST["password_confirmation"]
        if form["password"].value() != password2:
            message = "Passwords don't match"  # TODO: Probably need to change this to be more ambiguous
            return render(
                request,
                "register.html",
                {"user_registration_form": user_registration_form, "message": message},
            )

        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            email = form["email"].value()
            user = User.objects.create_user(username, password, email)  # type: ignore
            login(request, user)  # type: ignore
            return redirect("index")  # Needs to be made
        else:
            message = "Sorry something went wrong..."
            return render(
                request,
                "creation",
                {"user_registration_form": user_registration_form, "message": message},
            )

    else:
        return render(
            request, "register.html", {"user_registration_form": user_registration_form}
        )


@login_required(
    redirect_field_name="home/", login_url="login"
)  # Need to create the login html
def index(request):
    pass
