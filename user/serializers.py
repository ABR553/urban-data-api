from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'company_name', 'position_in_company', 'job_description', 'password')
        read_only_fields = ('id', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True}
        }