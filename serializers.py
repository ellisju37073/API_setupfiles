from rest_framework import serializers
from .models import Students

# Define a serializer for the Students model
class StudentSerializer(serializers.ModelSerializer):
    # Serializer field for first name, required and with a max length of 200 characters
    first_name = serializers.CharField(max_length=200, required=True)
    
    # Serializer field for last name, required and with a max length of 200 characters
    last_name = serializers.CharField(max_length=200, required=True)
    
    # Serializer field for address, required and with a max length of 200 characters
    address = serializers.CharField(max_length=200, required=True)
    
    # Serializer field for roll number, an integer field
    roll_number = serializers.IntegerField()
    
    # Serializer field for mobile number, required and with a max length of 10 characters
    mobile = serializers.CharField(max_length=10, required=True)

    # Meta class to specify the model and fields to be included in the serializer
    class Meta:
        model = Students  # Specify the model to be serialized
        fields = ('__all__')  # Include all fields from the model
