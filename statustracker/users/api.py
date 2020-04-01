from users.models import StatusTrackerUser
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# Lead Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = StatusTrackerUser.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer