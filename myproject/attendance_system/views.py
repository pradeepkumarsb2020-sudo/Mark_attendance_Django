from django.shortcuts import render, redirect
from .models import student, attendance
from datetime import date


def student_list(request):
    if request.method == "POST":
        student.objects.create(
            name=request.POST.get('name'),
            roll_no=request.POST.get('roll')
        )
        return redirect('students')

    students = student.objects.all()
    return render(
        request,
        'attendance/student_list.html',
        {'students': students}
    )


def mark_attendance(request):
    students = student.objects.all()
    today = date.today()

    if request.method == "POST":
        for stu in students:
            attendance.objects.update_or_create(
                student=stu,
                date=today,
                defaults={
                    'present': request.POST.get(str(stu.id)) == 'on'
                }
            )
        return redirect('attendance_list')

    return render(
        request,
        'attendance/mark_attendance.html',
        {'students': students, 'today': today}
    )


def attendance_list(request):
    records = attendance.objects.select_related('student').order_by('-date')
    return render(
        request,
        'attendance/attendance_list.html',
        {'records': records}
    )
