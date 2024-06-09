from django.shortcuts import render  # Import render function from Django shortcuts
from rest_framework.views import APIView  # Import APIView from Django REST framework
from rest_framework.response import Response  # Import Response from Django REST framework
from rest_framework import status  # Import status from Django REST framework
from .models import Students  # Import Students model
from .serializers import StudentSerializer  # Import StudentSerializer

# Create your views here.

# Define a view for handling requests related to the Students model
class StudentView(APIView):

    # Handle GET requests to retrieve all student records
    def get(self, request, *args, **kwargs):
        result = Students.objects.all()  # Query all student records
        serializers = StudentSerializer(result, many=True)  # Serialize the records
        return Response({'status': 'success', "students": serializers.data}, status=200)  # Return response with serialized data

    # Handle POST requests to create a new student record
    def post(self, request):
        serializer = StudentSerializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the new student record
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  # Return success response
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  # Return error response

# Define a view for handling requests related to a specific student record
class StudentView1(APIView):

    # Handle GET requests to retrieve a specific student record by ID
    def get(self, request, id):
        result = Students.objects.get(id=id)  # Query the student record by ID
        if id:  # Check if the ID is valid
            serializers = StudentSerializer(result)  # Serialize the record
            return Response({'success': 'success', "students": serializers.data}, status=200)  # Return response with serialized data

        result = Students.objects.all()  # Query all student records (this block is redundant and won't be executed)
        serializers = StudentSerializer(result, many=True)  # Serialize the records
        return Response({'status': 'success', "students": serializers.data}, status=200)  # Return response with serialized data

    # Handle PATCH requests to partially update a specific student record by ID
    def patch(self, request, id):
        result = Students.objects.get(id=id)  # Query the student record by ID
        serializer = StudentSerializer(result, data=request.data, partial=True)  # Deserialize the incoming data for partial update
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the updated student record
            return Response({"status": "success", "data": serializer.data})  # Return success response
        else:
            return Response({"status": "error", "data": serializer.errors})  # Return error response

    # Handle DELETE requests to delete a specific student record by ID
    def delete(self, request, id=None):
        result = Students.objects.get(id=id)  # Query the student record by ID
        result.delete()  # Delete the record
        return Response({"status": "success", "data": "Record Deleted"})  # Return success response indicating the record was deleted
