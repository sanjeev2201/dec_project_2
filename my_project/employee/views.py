from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
 # Create your views here.


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'New employee added Succesfully')
                return redirect('employees-list')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('employees-list')
            
    else:
        context = {
            'form': form
        }
        
        return render(request, 'employee/create.html', context)
def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(emp_id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(emp_id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)