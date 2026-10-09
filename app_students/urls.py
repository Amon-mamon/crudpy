from django.urls import path
from .views import StudentDeleteView, StudentView

urlpatterns = [
    path("student-list/", view=StudentView.as_view(), name="student_list"),
    path("student-delete/<int:id>/", view=StudentDeleteView.as_view(), name="student_delete")
]
