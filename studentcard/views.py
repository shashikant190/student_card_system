from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import StudentRegistration
from .models import StudentCard

# For index
def index(request):
    return render(request, 'index.html')


# For student registration
def studentregistration(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Create StudentRegistration entry
            student = StudentRegistration.objects.create(name=name, email=email, password=password)
            # Create User entry for authentication
            user = User.objects.create_user(username=email, email=email, password=password)
            # Automatically set the user as staff if they are not a superuser
            if not user.is_superuser:
                user.is_staff = True
            user.save()

            return redirect('studentlogin_html')
        except Exception as e:
            error = str(e)
    return render(request, 'studentregistration.html', {'error': error})

# For student login
def studentlogin(request):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'studentlogin.html', {'error': error})

# For student dashboard
from django.contrib.auth.decorators import login_required
@login_required
def studentdashboard(request):
    user = request.user
    return render(request, 'studentdashboard.html', {'user': user})

# For logout
from django.contrib.auth import logout

def studentlogout(request):
    logout(request)
    return redirect('index')


# For barcode 
# import time
# from barcode import Code128
# from barcode.writer import ImageWriter
# from django.http import HttpResponse

# def generate_unique_barcode():
    # Generate a unique barcode based on current timestamp
    # timestamp = str(int(time.time()))  # Get current timestamp
    # barcode_value = f'STUDENT-{timestamp}'  # Example format: STUDENT-1642705536

    # Generate barcode image using Code128 format
    # barcode = Code128(barcode_value, writer=ImageWriter())
    # barcode_filename = f'static/barcodes/{barcode_value}.png'

    # Save the barcode image
    # barcode_path = barcode.save(barcode_filename)

    # return barcode_value


# For student card
# For student card
from django.contrib import messages
def studentcard(request):
    error = ""  # Define error variable here
    if request.method == 'POST':
        first_name = request.POST['first_name']
        father_name = request.POST['father_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
#         barcode = request.POST.get('barcode')
        try:
            studentcard = StudentCard.objects.create(
                first_name=first_name,
                father_name=father_name,
                last_name=last_name,
                dob=dob,
                phone_number=phone_number,
                address=address,
            )
            error = "no"
            messages.success(request, 'Student card generated successfully.')
            return redirect('studentdashboard_html')
        except Exception as e:
            error = "yes"
            messages.error(request, f"Failed to generate student card: {str(e)}")
    return render(request, 'studentcard.html', {'error': error})

# To view student card data

def viewstudentcard(request):
    return render(request, 'viewstudentcard.html')