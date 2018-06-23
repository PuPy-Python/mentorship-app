from django.shortcuts import render


def show_homepage_view(request):
    """Homepage view.

    Display the homepage template for PuPPy Mentorship."""

    return render(request, "mentorship/homepage.html")


def show_CoC_view(request):
    """Code of conduct view.

    Display the code of conduct page."""

    return render(request, "mentorship/conduct.html")
