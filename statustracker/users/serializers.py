from rest_framework import serializers

from users.models import StatusTrackerUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusTrackerUser
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth', 'department']