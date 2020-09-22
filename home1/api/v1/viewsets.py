from rest_framework import authentication
from home1.models import US
from .serializers import USSerializer
from rest_framework import viewsets


class USViewSet(viewsets.ModelViewSet):
    serializer_class = USSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = US.objects.all()
