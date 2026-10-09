from django.shortcuts import get_object_or_404, render
from . models import Student
# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import StudentForm
from django.shortcuts import redirect


class StudentView(ListView):
    model = Student
    template_name= "student_list.html"
    context_object_name="students"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = kwargs.get("form", StudentForm())
        context["student"] = kwargs.get("student")
        
        return context
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
        student_id = request.GET.get("edit")
        student=None
        
        if student_id:
            student = get_object_or_404(Student, id=student_id)
            form = StudentForm(instance=student)
        else:
            form = StudentForm()
            
        return self.render_to_response(
            self.get_context_data(form=form, student=student)
        )
        
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
        student_id = request.POST.get("student_id")
        student = None
        
        if student_id:
            student = get_object_or_404(Student, id=student_id)
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect("student_list")

        return self.render_to_response( self.get_context_data(
            form=form, student=student
        ))
      
    
class StudentDeleteView(View):
    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
    
        return redirect('student_list')

