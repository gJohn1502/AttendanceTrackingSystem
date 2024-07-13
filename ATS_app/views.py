from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
import random
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from matplotlib import pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from django.http import FileResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import plotly.graph_objs as go
from plotly.offline import plot
import io



from django.db import models

from .forms import StudentRegistrationForm
from .forms import StudentLoginForm
from .forms import TeacherRegistrationForm
from .forms import TeacherLoginForm
from .forms import ParentRegistrationForm
from .forms import ParentLoginForm
from .forms import AddAttendanceForm

from .models import PARENT
from .models import STUDENT
from .models import STUDENT_INFO
from .models import TEACHER
from .models import ATTENDANCE_DATA

from .resources import PARENTResource
from .resources import StudentAndInfoResource
from .resources import TEACHERResource
from .resources import ATTENDANCEResource
from django.contrib import messages
from tablib import Dataset
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from plotly.offline import plot

from openpyxl import load_workbook
from django.utils import timezone
# from tablib import Dataset

# from .models import ATTENDANCE_INFO
# from .resources import ATTENDANCEResource
# Create or update an instance of YourModel with date_field set to the current date
#-----------------------------------------------------------------
def student_login(request):
        if request.method == 'POST':
            form = StudentLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Student_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = StudentLoginForm()
        loginform = form
        return render(request,'student_login.html',{'loginform': loginform })
        
def student_register(request):
        if request.method == 'POST':
            form = StudentRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    student = STUDENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if student is not None:
                        random_number = random.randint(100, 999)
                        username = student.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=student.FIRST_NAME, last_name=student.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'Student not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
        else: 
            form = StudentRegistrationForm()
            # loginform = StudentLoginForm()
        registerform = form 
        return render(request,'student_register.html',{'registerform': registerform })

def parent_login(request):
        if request.method == 'POST':
            form = ParentLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Parent_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = ParentLoginForm()
        loginform = form
        return render(request,'parent_login.html',{'loginform': loginform })
        
def parent_register(request):
    if request.method == 'POST':
            form = ParentRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    parent = PARENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if parent is not None:
                        random_number = random.randint(100, 999)
                        username = parent.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=parent.FIRST_NAME, last_name=parent.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'parent not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
    else: 
            form = ParentRegistrationForm()
            # loginform = StudentLoginForm()
    registerform = form 
    return render(request,'parent_register.html',{'registerform': registerform })

def teacher_login(request):
        if request.method == 'POST':
            form = TeacherLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Teacher_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = TeacherLoginForm()
        loginform = form
        return render(request,'teacher_login.html',{'loginform': loginform })

def teacher_register(request):
        if request.method == 'POST':
            form = TeacherRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    teacher = TEACHER.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if teacher is not None:
                        random_number = random.randint(100, 999)
                        username = teacher.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=teacher.FIRST_NAME, last_name=teacher.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'teacher not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
        else: 
            form = TeacherRegistrationForm()
            # loginform = StudentLoginForm()
        registerform = form 
        return render(request,'teacher_register.html',{'registerform': registerform })

#--------------------------------------------------------------------------------

def PARENT_upload(request):
    if request.method == 'POST':
        # Clear existing messages
        storage = messages.get_messages(request)
        storage.used = True

        PARENT_resource = PARENTResource()
        dataset = Dataset()
        new_PARENT = request.FILES['myfile']

        if not new_PARENT.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'attendance_entry.html')

        try:
            imported_data = dataset.load(new_PARENT.read(),format='xlsx')
            for data in imported_data:
                value = PARENT(
                    PARENT_ID=data[0],
                    FIRST_NAME=data[1],
                    LAST_NAME=data[2],
                    PHONE_NO=data[3],
                    EMAIL_ADDRESS=data[4]
                )
                value.save()
            messages.success(request, 'Parent data uploaded successfully.')

        except IntegrityError as ie:
            messages.error(request, f'Data is not unique. Please check your input: {str(ie.args[1])}')
        except ValueError as ve:
            messages.error(request, f'Unsupported data type. Please check your input: {str(ve)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request,'attendance_entry.html')
    
def StudentAndInfo_upload(request):
    # Clear existing messages
    storage = messages.get_messages(request)
    storage.used = True

    if request.method == 'POST':
        STUDENT_resource = StudentAndInfoResource()
        dataset = Dataset()
        new_STUDENT = request.FILES['myfile']

        if not new_STUDENT.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'attendance_entry.html')
        
        try:
            imported_data = dataset.load(new_STUDENT.read(),format='xlsx')
            for data in imported_data:
                parent_id = data[3]  # Assuming data[3] contains the parent_id
                try:
                    parent = PARENT.objects.get(pk=parent_id)
                except PARENT.DoesNotExist:
                    messages.error(request, f"Parent with ID {parent_id} does not exist.")
                    return render(request, 'attendance_entry.html')
                student = STUDENT(
                    STUDENT_ID=data[0],
                    FIRST_NAME=data[1],
                    LAST_NAME=data[2],
                    PARENT_ID=parent,
                    EMAIL_ADDRESS=data[4]
                )
                student.save()
                student_id = data[0]  # Assuming data[3] contains the parent_id
                try:
                    student = STUDENT.objects.get(pk=student_id)
                except STUDENT.DoesNotExist:
                    messages.error(request, f"Student with ID {student_id} does not exist.")
                    return render(request, 'attendance_entry.html')
                student_info = STUDENT_INFO(
                    STUDENT_ID=student,
                    DEPARTMENT=data[5],
                    SECTION=data[6]
                )
                student_info.save()
            messages.success(request, 'Student data uploaded successfully.')
        except IntegrityError as ie:
            messages.error(request, f'Data is not unique. Please check your input: {str(ie.args[1])}')
        except ValueError as ve:
            messages.error(request, f'Unsupported data type. Please check your input: {str(ve)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request,'attendance_entry.html')
    
def TEACHER_upload(request):
    # Clear existing messages
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        TEACHER_resource = TEACHERResource()
        dataset = Dataset()
        new_TEACHER = request.FILES['myfile']

        if not new_TEACHER.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'attendance_entry.html')
        
        try:
            imported_data = dataset.load(new_TEACHER.read(),format='xlsx')
            for data in imported_data:
                value = TEACHER(
                    TEACHER_ID=data[0],
                    FIRST_NAME=data[1],
                    LAST_NAME=data[2],
                    PHONE_NO=data[3],
                    EMAIL_ADDRESS=data[4]
                )
                value.save()
            messages.success(request, 'Teacher data uploaded successfully.')
        except IntegrityError as ie:
            print(ie.args[1])
            messages.error(request, f'Data is not unique. Please check your input: {str(ie.args[1])}')
        except ValueError as ve:
            messages.error(request, f'Unsupported data type. Please check your input: {str(ve)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request,'attendance_entry.html')
    
def ATTENDANCE_upload(request):
    # Clear existing messages
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        ATTENDANCEresource = ATTENDANCEResource()
        dataset = Dataset()
        new_ATTENDANCE = request.FILES['myfile']

        if not new_ATTENDANCE.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'attendance_entry.html')
        
        try:
            imported_data = dataset.load(new_ATTENDANCE.read(),format='xlsx')
            for data in imported_data:
                student_id = data[0]
                try:
                    student = STUDENT.objects.get(pk=student_id)
                except STUDENT.DoesNotExist:
                    messages.error(request, f"Student with ID {student_id} does not exist.")
                    return render(request, 'attendance_entry.html')
                value = ATTENDANCE_DATA(
                    STUDENT_ID=student,
                    FIRST_NAME=data[1],
                    LAST_NAME=data[2],
                    DATE=data[3],
                    HOUR1=data[4],
                    HOUR2=data[5],
                    HOUR3=data[6],
                    HOUR4=data[7],
                    HOUR5=data[8],
                    HOUR6=data[9],
                    HOUR7=data[10],
                    HOUR8=data[11],
                )
                value.save()
            messages.success(request, 'Attendance data uploaded successfully.')
        except IntegrityError as ie:
            messages.error(request, f'Data is not unique. Please check your input: {str(ie.args[1])}')
        except ValueError as ve:
            messages.error(request, f'Unsupported data type. Please check your input: {str(ve)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    return render(request,'attendance_entry.html')

def attendance_pie(request):
    try:
        attendance_data = ATTENDANCE_DATA.objects.get(STUDENT_ID=20001, DATE="2024-04-03")
    except ATTENDANCE_DATA.DoesNotExist:
        return HttpResponse('Attendance data not found for the given student and date')

    # Count the occurrences of each status (present, absent, od)
    status_counts = {'PRESENT': 0, 'ABSENT': 0, 'ON DUTY': 0}
    for hour in range(1, 9):
        status = getattr(attendance_data, f'HOUR{hour}', None)
        if status == 'PRESENT':
            status_counts['PRESENT'] += 1
        elif status == 'ABSENT':
            status_counts['ABSENT'] += 1
        elif status == 'ON DUTY':
            status_counts['ON DUTY'] += 1

    if not any(status_counts.values()):
        # No valid data for the pie chart
        return HttpResponse('No attendance data available for the given student and date')

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%', startangle=90)
    plt.title(f'Attendance Status for Student {20001} on {"2024-04-03"}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.savefig('static/plots/attendance.png')  # Save the plot as a PNG file
    plt.close()

    # Pass the path to the saved plot to the template
    context = {'plot_path': 'static/plots/attendance.png'}

    # Render the template with the plot
    return render(request, 'dashboard.html', context)

def overall_attendance(request):
    # Fetch the attendance data
    attendance_data = ATTENDANCE_DATA.objects.all()

    # Convert attendance data to a DataFrame
    attendance_df = pd.DataFrame(list(attendance_data.values()))

    # Calculate total present and absent students for each date
    attendance_df['total_present'] = attendance_df.apply(lambda row: sum(row['HOUR1':'HOUR8'] == 'PRESENT'), axis=1)
    attendance_df['total_absent'] = attendance_df.apply(lambda row: sum(row['HOUR1':'HOUR8'] == 'ABSENT'), axis=1)

    # Group by date and calculate total present and absent students for each date
    total_attendance = attendance_df.groupby('DATE').agg({
    'total_present': 'sum',
    'total_absent': 'sum'
    }).reset_index()
    fig = px.line(
        total_attendance,
        x='DATE', 
        y=['total_present', 'total_absent'],

        labels={'date': 'Date', 'value': 'Number of Students', 'variable': 'Attendance Status'},
        title='Overall Attendance Trends')
    chart = fig.to_html()
    context ={'chart':chart}

    return render(request, 'overall_attendance.html', context)
    #return render(request,'overall_attendance.html')

def attendance_status(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        # if selected_date == '' or len(queryset) == 0:
        #     error = {'error' : 'No data on this date'}
        #     return render(request, 'attendance_status.html', error)
        # Filter the queryset to get attendance data for the specific date
        queryset = ATTENDANCE_DATA.objects.filter(DATE=selected_date)

        # Convert the attendance data to a pandas DataFrame
        df = pd.DataFrame(queryset.values('STUDENT_ID', 'HOUR1', 'HOUR2', 'HOUR3', 'HOUR4', 'HOUR5', 'HOUR6', 'HOUR7', 'HOUR8'))

        # Calculate total hours attended per student
        df['total_hours'] = df[['HOUR1', 'HOUR2', 'HOUR3', 'HOUR4', 'HOUR5', 'HOUR6', 'HOUR7', 'HOUR8']].apply(lambda row: row.str.count('PRESENT')).sum(axis=1)

        # Classify students as 'Present' or 'Absent' based on total hours attended
        df['status'] = df['total_hours'].apply(lambda x: 'PRESENT' if x >= 4 else 'ABSENT')

        # Calculate the count of 'Present' and 'Absent' students
        status_counts = df['status'].value_counts()

        # Create the pie chart
        fig = px.pie(names=status_counts.index, values=status_counts.values, title=f'Attendance Status Distribution on {selected_date}')

        # Convert the plot to HTML
        chart = fig.to_html()
        context = {'chart': chart}
        return render(request, 'attendance_status.html', context)
    return render(request, 'attendance_status.html')

def attendance_tracking(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        # if selected_date == '' or len(queryset) == 0:
        #     error = {'error' : 'No data on this date'}
        #     return render(request, 'attendance_status.html', error)
        # Filter the queryset to get attendance data for the specific date
        # Filter the attendance data for the specific date
        attendance_data = ATTENDANCE_DATA.objects.filter(DATE=selected_date)
        
        # Filter the attendance data to get only the students who are absent in the afternoon session
        absent_students = attendance_data.exclude(HOUR5='PRESENT', HOUR6='PRESENT', HOUR7='PRESENT', HOUR8='PRESENT')

        # Create a list of student names and the total number of hours they are absent in the afternoon session
        student_names = []
        hours_absent = []
        for student in absent_students:
            total_absent_hours = sum([1 for hour in ['HOUR5', 'HOUR6', 'HOUR7', 'HOUR8'] if getattr(student, hour) != 'PRESENT'])
            if total_absent_hours > 0:
                student_names.append(student.FIRST_NAME)
                hours_absent.append(total_absent_hours)

        # Create hover text with student name and hours absent
        hover_text = [f'{name}<br>Hours Absent: {hours}' for name, hours in zip(student_names, hours_absent)]

        # Create the Plotly bar chart with a bar for each student
        fig = go.Figure(data=[go.Bar(x=student_names, y=hours_absent, hovertext=hover_text, hoverinfo='text', marker_color='orange')])
        fig.update_layout(title=f'Number of Hours Students are Absent in Afternoon Session on {selected_date}',
                          xaxis_title='Student Name',
                          yaxis_title='Number of Hours Absent',
                          bargap=0.1)

        # Convert the Plotly chart to HTML
        chart = plot(fig, output_type='div', include_plotlyjs=False)
        context = {'chart': chart}
        return render(request, 'attendance_tracking.html', context)
    return render(request, 'attendance_tracking.html')


def daily_attendance(request):
    if request.method == 'POST':
    # Assuming 'date' and 'selected_date' are provided as inputs
        selected_date = request.POST.get('date')
        if selected_date == '' or None:
            error = {'error' : 'No data on this date'}
            return render(request, 'daily_attendance.html', error)

        attendance_data = ATTENDANCE_DATA.objects.filter(DATE=selected_date).values('FIRST_NAME', 'HOUR1', 'HOUR2', 'HOUR3', 'HOUR4', 'HOUR5', 'HOUR6', 'HOUR7', 'HOUR8')
        if selected_date == '' or len(attendance_data) == 0:
            error = {'error' : 'No data on this date'}
            return render(request, 'daily_attendance.html', error)
        # Convert the attendance data to a pandas DataFrame
        df = pd.DataFrame(attendance_data)
        print(df)
        # Calculate total hours attended per student
        df['total_hours'] = df[['HOUR1', 'HOUR2', 'HOUR3', 'HOUR4', 'HOUR5', 'HOUR6', 'HOUR7', 'HOUR8']].apply(lambda row: row.str.count('PRESENT' or 'ON DUTY')).sum(axis=1)

        # Get student names and total hours
        student_names = df['FIRST_NAME']
        total_hours = df['total_hours']

        for student in attendance_data:
            print(student_names,total_hours)
        # Create a Plotly bar chart
        fig = px.bar(x=student_names, y=total_hours, labels={'x': 'Student Name', 'y': 'Total Hours Attended'},
                     title=f'Total Hours Attended per Student on {selected_date}')
        fig.update_layout(xaxis={'categoryorder': 'total ascending', 'type': 'category', 'tickangle': 45,
                                 'title': 'Student Name', 'automargin': True},
                          yaxis={'title': 'Total Hours Attended', 'range': [0, 8]},
                          width=1200, height=600, margin={'l': 50, 'r': 50, 't': 50, 'b': 50})

        # Convert the Plotly chart to JSON format for rendering in the template
        chart = fig.to_html()

        context = {'chart': chart}
        return render(request, 'daily_attendance.html', context)
    return render(request, 'daily_attendance.html')
#-----------------------------------------------------------------------------------------
def home(request):
    return render(request,'index.html')

def login_as(request):
    return render(request,'choicelogin.html')

def teacher_dashboard(request):
    return render(request,'teacher_page.html')

def parent_dashboard(request):
    return render(request,'parent_page.html')

def student_dashboard(request):
    return render(request,'student_page.html')

def dashboard(request):
    return render(request,'dashboard_home.html')

def about_us(request):
    return render(request,'about1.html')

def help_support(request):
    return render(request, 'helpsupport.html')

def direct_or_excel(request):
    return render(request, 'direct_or_excel.html')

@login_required
def attendance_entry(request):
    return render(request, 'attendance_entry.html')


def add_attendance(request):
    # form = AddAttendanceForm(request.POST or None)
    departments = STUDENT_INFO.objects.values_list('DEPARTMENT', flat=True).distinct()
    sections = STUDENT_INFO.objects.values_list('SECTION', flat=True).distinct()
    if request.method == 'POST':
        # form = AddAttendanceForm(request.POST)
        # if form.is_valid():
        # department = form.cleaned_data['department']
        # section = form.cleaned_data['section']
        # date = form.cleaned_data['date']
        department = request.POST.get('department')
        section = request.POST.get('section')
        date = request.POST.get('date')
        print(department)
        print(section)
        print(date)
        students = STUDENT.objects.filter(student_info__DEPARTMENT=department, student_info__SECTION=section)
        print(students)
        for student in students:
            attendance_data = ATTENDANCE_DATA(
                STUDENT_ID=student,
                FIRST_NAME=student.FIRST_NAME,
                LAST_NAME=student.LAST_NAME,
                DATE=date,
                HOUR1=request.POST.get(f"hour1_{student.STUDENT_ID}"),
                HOUR2=request.POST.get(f"hour2_{student.STUDENT_ID}"),
                HOUR3=request.POST.get(f"hour3_{student.STUDENT_ID}"),
                HOUR4=request.POST.get(f"hour4_{student.STUDENT_ID}"),
                HOUR5=request.POST.get(f"hour5_{student.STUDENT_ID}"),
                HOUR6=request.POST.get(f"hour6_{student.STUDENT_ID}"),
                HOUR7=request.POST.get(f"hour7_{student.STUDENT_ID}"),
                HOUR8=request.POST.get(f"hour8_{student.STUDENT_ID}"),
            )
            attendance_data.save()
        return render(request, 'success.html')
    return render(request, 'add_attendance.html', {'departments': departments, 'sections': sections})

def fetch_students(request):
    department = request.GET.get('department')
    section = request.GET.get('section')
    print("working")
    students = STUDENT.objects.filter(student_info__DEPARTMENT=department, student_info__SECTION=section)
    student_data = []
    for student in students:
        student_data.append({
            'student_id': student.STUDENT_ID,
            'first_name': student.FIRST_NAME,
            'last_name': student.LAST_NAME
        })
    print(student_data)
    
    return JsonResponse(student_data, safe=False)

def calculate_summary(student_id, start_date=None, end_date=None):
    # Filter the attendance data for the specific student and date range
    if start_date and end_date:
        attendance_data = ATTENDANCE_DATA.objects.filter(STUDENT_ID=student_id, DATE__range=[start_date, end_date])
    else:
        attendance_data = ATTENDANCE_DATA.objects.filter(STUDENT_ID=student_id)
    
    if not attendance_data:
        return {
            'student_id': student_id,
            'total_days': 0,
            'total_no_of_hours': 0,
            'total_hours_attended': 0,
            'percentage':0,
        }
    # Convert the filtered attendance data to a pandas DataFrame
    df = pd.DataFrame(list(attendance_data.values('DATE', 'HOUR1', 'HOUR2', 'HOUR3', 'HOUR4', 'HOUR5', 'HOUR6', 'HOUR7', 'HOUR8')))
    
    # Omit duplicate dates and consider only HOUR1 with values present or absent
    unique_dates_attended = df['DATE'].unique()
    total_days = len(unique_dates_attended)
    
    # Calculate the total number of hours attended
    total_hours_attended = 0
    for date in unique_dates_attended:
        hours_present = (df[df['DATE'] == date].iloc[:, 1:] == 'PRESENT').astype(int).sum().sum()
        total_hours_attended += hours_present
    print(total_hours_attended)
    if (total_days != 0 ):
        percentage = (total_hours_attended / (total_days * 8)) * 100
        percentage = round(percentage, 2)
    else:
        percentage = 0
    return {
        'student_id': student_id,
        'total_days': total_days,
        'total_no_of_hours': total_days * 8,
        'total_hours_attended': total_hours_attended,
        'percentage':percentage,
    } 
def attendance_summary(request):
    student_id = request.GET.get('student_id')  # Replace with the actual student ID
    start_date = request.GET.get('start_date')  # Get start date from request
    end_date = request.GET.get('end_date')  # Get end date from request

    # Calculate summary for the specified student and date range
    summary = calculate_summary(student_id, start_date, end_date)

    # Create a Plotly pie chart
    labels = ['Days Present', 'Days Absent']
    values = [summary['total_hours_attended'], summary['total_no_of_hours'] - summary['total_hours_attended']]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    chart = plot(fig, output_type='div', include_plotlyjs=False)

    context = {'chart': chart, 'summary': summary}
    return render(request, 'attendance_summary.html', context)


def generate_report(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        
        # Calculate summary for the specified student and date range
        summary = calculate_summary(student_id)

        # Create a Plotly pie chart
        labels = ['Days Present', 'Days Absent']
        values = [summary['total_hours_attended'], summary['total_no_of_hours'] - summary['total_hours_attended']]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
        chart_div = plot(fig, output_type='div', include_plotlyjs=False)
        fig.update_layout(width=456, height=636)

        # Generate PDF report
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        # Title
        elements.append(Paragraph("Attendance Report", styles['Title']))

        elements.append(Spacer(1, 12))

        # Plotly Pie Chart
        elements.append(Paragraph("Attendance Summary", styles['Heading2']))

        elements.append(Paragraph(f"Student ID: {student_id}", styles['Heading1']))
        elements.append(Paragraph(f"Total Number of days: {summary['total_days']}", styles['Heading1']))
        elements.append(Paragraph(f"Total Number of Hours: {summary['total_no_of_hours']}", styles['Heading1']))
        elements.append(Paragraph(f"Number of Hours Attended: {summary['total_hours_attended']}", styles['Heading1']))
        elements.append(Paragraph(f"Percentage: {summary['percentage']}", styles['Heading1']))

        # Convert the Plotly chart to an image and add it to the PDF
        img_bytes = fig.to_image(format="png")
        img_stream = io.BytesIO(img_bytes)
        chart_image = Image(img_stream)
        chart_image = Image(img_stream, width=456, height=636)
        elements.append(chart_image)

        elements.append(Spacer(1, 12))

        # Add elements to the PDF document
        doc.build(elements)

        # Reset buffer position and return FileResponse
        buf.seek(0)
        return FileResponse(buf, as_attachment=True, filename='report.pdf')
    else:
        # Render HTML template for initial page load
        return render(request, 'generate_report.html')


# def generate_total_report(request):
#     if request.method == 'POST':
#         # Calculate summary for all students
#         students = STUDENT.objects.all()
#         student_summaries = []
#         for student in students:
#             student_id = student.STUDENT_ID
#             summary = calculate_summary(student_id)
#             if summary['total_days'] == 0:
#                 continue 
#             student_summary = [
#                 student_id,
#                 summary['total_days'],
#                 summary['total_no_of_hours'],
#                 summary['total_hours_attended'],
#                 summary['percentage'] , 
#             ]
#             student_summaries.append(student_summary)

#         # Create a table with headers
#         table_data = [['Student ID', 'Total Days', 'Total Hours', 'Hours Attended', 'Percentage']]
#         table_data.extend(student_summaries)

#         # Generate PDF report with the table
#         buf = BytesIO()
#         doc = SimpleDocTemplate(buf, pagesize=letter)
#         styles = getSampleStyleSheet()

#         elements = []
#         elements.append(Paragraph("Attendance Report", styles['Title']))
#         elements.append(Spacer(1, 12))
#         elements.append(Paragraph("Attendance Summary for All Students", styles['Heading2']))

#         # Create table
#         # table = Table(table_data)
#         table = Table(table_data, colWidths=[200, 200], rowHeights=30)
#         table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
#                                    ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))]))
        
#         table.wrapOn(doc, doc.width, doc.height)
#         table_width, table_height = table.wrap(doc.width, doc.height)
#         table.drawOn(doc, (doc.width - table_width) / 2, doc.height - table_height - 100)
        
#         elements.append(table)
#         doc.build(elements)

#         # Reset buffer position and return FileResponse
#         buf.seek(0)
#         return FileResponse(buf, as_attachment=True, filename='report.pdf')
#     else:
#         # Render HTML template for initial page load
#         return render(request, 'generate_total_report.html')

def generate_total_report(request):
    if request.method == 'POST':
        # Calculate summary for all students
        students = STUDENT.objects.all()
        student_summaries = []
        for student in students:
            student_id = student.STUDENT_ID
            student_name = student.FIRST_NAME  # Assuming 'STUDENT_ID' is the correct field name
            summary = calculate_summary(student_id)
            if summary['total_days'] == 0 :
                continue
            student_summary = [
                student_id,
                student_name,
                summary['total_days'],
                summary['total_no_of_hours'],
                summary['total_hours_attended'],
                summary['percentage'],
            ]
            student_summaries.append(student_summary)

        # Create a table with headers
        table_data = [['Student ID','Student Name', 'Total Days', 'Total Hours', 'Hours Attended', 'Percentage']]
        table_data.extend(student_summaries)

        # Generate PDF report with the table
        buf = BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []
        elements.append(Paragraph("Attendance Report", styles['Title']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Attendance Summary for All Students", styles['Heading2']))

        # Create table
        table = Table(table_data, colWidths=[None, None, None, None, None], rowHeights=30)
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
                                   ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))]))

        elements.append(table)

        # Build PDF document
        doc.build(elements)

        # Reset buffer position and return FileResponse
        buf.seek(0)
        return FileResponse(buf, as_attachment=True, filename='report.pdf')
    else:
        # Render HTML template for initial page load
        return render(request, 'generate_total_report.html')
