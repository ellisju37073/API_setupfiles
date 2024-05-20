from .views import StudentView
from .views import StudentView1
from django.urls import path

urlpatterns = [
    path('basic/', StudentView.as_view()),
    path('basic/<int:id>/', StudentView1.as_view())
]  