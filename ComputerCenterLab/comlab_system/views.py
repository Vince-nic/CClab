from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Count
from .models import *

# ----------------------- login page -------------------------------------------


def login_view(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            user = Account.objects.get(account_id=user_id)
            if user.role == 'admin':
                return redirect('admin_dashboard') 
            elif user.role == 'personnel':
                return redirect('lab_dashboard_view')  
        except Account.DoesNotExist:
            request.session.flush() 
            return redirect('login_view')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(username=username, password=password)
            request.session['user_id'] = user.account_id
            request.session['role'] = user.role

            if user.role == 'admin':
                return redirect('admin_dashboard')  
            elif user.role == 'personnel':
                return redirect('lab_dashboard_view')  
        except Account.DoesNotExist:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

def logout_user(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login_view') 
# ------------------------ navigation display ----------------------------------

def navigation(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_view') 

    try:
        user = Account.objects.get(account_id=user_id)
    except Account.DoesNotExist:
        user = None
        messages.error(request, 'User not found.')

    context = {
        'user': user
    }

    return render(request, 'navigation.html', context)

# ------------------------ laboratory list -------------------------------------
def lab_dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_view') 

    try:
        user = Account.objects.get(account_id=user_id)
    except Account.DoesNotExist:
        user = None
        messages.error(request, 'User not found.')

    computer_labs = ComputerLab.objects.all()

    # Add unit count to each lab object
    for lab in computer_labs:
        lab.unit_count = Unit.objects.filter(computerlab=lab).count()

    context = {
        'computer_labs': computer_labs,
        'user': user
    }

    return render(request, 'labSelection.html', context)



# ------------------------- computer lab dashboard -----------------------------

def dashboard_view(request, lab_id=None):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login_view')  

    try:
        user = Account.objects.get(account_id=user_id)
    except Account.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('login_view') 

    computer_labs = ComputerLab.objects.all()

    lab_name = "All Labs" 
    units = Unit.objects.select_related('computerlab', 'component__status').all()

    if lab_id:  
        try:
            lab = ComputerLab.objects.get(pk=lab_id)
            units = Unit.objects.select_related('computerlab', 'component__status').filter(computerlab=lab)
            lab_name = lab.lab
        except ComputerLab.DoesNotExist:
            messages.error(request, 'lab does not exist.')
            return redirect('dashboard_view') 

    context = {
        'computer_labs': computer_labs,
        'units': units,
        'user': user,
        'selected_lab': lab_id,
        'lab_name': lab_name,
    }

    return render(request, 'dashboard.html', context)



# --------------------------- function for saving checkbox --------------

def update_status(request):
    if request.method == 'POST':
        status_id = request.POST.get('status_id')
        monitor_status = request.POST.get('monitorStatus')
        keyboard_status = request.POST.get('keyboardStatus')
        mouse_status = request.POST.get('mouseStatus')
        ram_status = request.POST.get('ramStatus')
        motherboard_status = request.POST.get('motherboardStatus')
        cpu_status = request.POST.get('cpuStatus')
        remarks = request.POST.get('remarks')
        lab = request.POST.get('computerlab_id')

        try:
            status = Status.objects.get(status_id=int(status_id))  
        except Status.DoesNotExist:
            messages.error(request, 'Status not found.')
            return redirect('dashboard_view')

        # Update the status fields
        status.stat_monitor = monitor_status
        status.stat_keyboard = keyboard_status
        status.stat_mouse = mouse_status
        status.stat_ram = ram_status
        status.stat_motherboard = motherboard_status
        status.stat_cpu = cpu_status
        status.remarks = remarks
        status.date = timezone.now().date()  
        status.time = timezone.now().time()   

        status.save()

        messages.success(request, 'Status updated successfully.')
        return redirect(f'dashboard/lab/{lab}/') 

    return redirect('dashboard_view')

# ---------------- function for adding units-----------------

def add_unit(request):
    if request.method == "POST":
        pc_number = request.POST.get('pc_number')
        monitor = request.POST.get('monitor')
        keyboard = request.POST.get('keyboard')
        mouse = request.POST.get('mouse')
        ram = request.POST.get('ram')
        motherboard = request.POST.get('motherboard')
        cpu = request.POST.get('cpu')
        lab_id = request.POST.get('computerlab_id')  
        Functional = request.POST.get('status') 

        if not lab_id:
            return HttpResponse("Lab ID is missing", status=400)  

        status = Status(
            remarks="", 
            date=timezone.now().date(),
            time=timezone.now().time(),
            stat_monitor=Functional,
            stat_keyboard=Functional,
            stat_mouse=Functional,
            stat_ram=Functional,
            stat_motherboard=Functional,
            stat_cpu=Functional,
        )
        status.save()

        component = Components(
            monitor=monitor,
            keyboard=keyboard,
            mouse=mouse,
            ram=ram,
            motherboard=motherboard,
            cpu=cpu,
            status=status  
        )
        component.save()

        try:
            computer_lab = ComputerLab.objects.get(computerlab_id=lab_id)  

            unit = Unit(
                computerlab=computer_lab,
                component=component,
                pc_number=pc_number
            )
            unit.save()

            return redirect(f'/dashboard/lab/{lab_id}/') 
            
        except ComputerLab.DoesNotExist:
            return HttpResponse("Computer Lab not found", status=404)

    return render(request, 'dashboard.html')