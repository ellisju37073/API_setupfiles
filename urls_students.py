from .views import StudentView  # Importing the StudentView class from views
from .views import StudentView1  # Importing the StudentView1 class from views
from django.urls import path  # Importing the path function from django.urls

# Define URL patterns for the API endpoints
urlpatterns = [
    # URL pattern for accessing the basic student view, which handles all students
    path('basic/', StudentView.as_view()),
    
    # URL pattern for accessing a specific student view based on the student's ID
    path('basic/<int:id>/', StudentView1.as_view())
]
