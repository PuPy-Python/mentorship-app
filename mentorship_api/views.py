from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hello_world(request):
    """Get for the hello world test."""
    return Response({'message': 'Hello World!'})


@api_view()
def login(request):
    """Received login request."""
    return Response({'message': 'Login attempt received.'})
