from django.views.generic import  CreateView
from django.urls import reverse_lazy

# from collageapp.models import Course, Center
from .models import Student1, Subcenter, Total_fees
from .forms import StudentForm
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def next(request):
    return render(request,"next.html")

class StudentCreateView(CreateView):
    model = Student1
    template_name = '1student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('result1')

def load_branches(request):
    center_id = request.GET.get('center')
    subcenters = Subcenter.objects.filter(center_id=center_id).order_by('name')
    return render(request, '1branch_dropdown_list_options.html', {'subcenters': subcenters})

def load_fees(request):
    course1_id = request.GET.get('course1')
    total_fees = Total_fees.objects.filter(course1_id=course1_id).order_by('name')
    return render(request, '1fees.html', {'total_fees': total_fees})

def result1(request):
    return render(request,"result.html")