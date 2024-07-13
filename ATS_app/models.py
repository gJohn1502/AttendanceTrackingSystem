from django.db import models
from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits.',
)

class PARENT(models.Model):
    PARENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=10, validators=[phone_number_validator], unique=True)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.PARENT_ID}"

class STUDENT(models.Model):
    STUDENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PARENT_ID = models.ForeignKey(PARENT, on_delete=models.CASCADE)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.STUDENT_ID}"

class STUDENT_INFO(models.Model):
    STUDENT_ID = models.OneToOneField(STUDENT, primary_key=True, on_delete=models.CASCADE)
    DEPARTMENT = models.CharField(max_length=255)
    SECTION = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.STUDENT_ID}"

class TEACHER(models.Model):
    TEACHER_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=10, validators=[phone_number_validator],unique=True)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.TEACHER_ID}"

class ATTENDANCE_DATA(models.Model):
    id = models.AutoField(primary_key=True)
    STUDENT_ID = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    FIRST_NAME = models.CharField(max_length=255 , null=False)
    LAST_NAME = models.CharField(max_length=255, default='')
    DATE = models.DateField()
    HOUR1 = models.CharField(max_length=255, default='NULL')
    HOUR2 = models.CharField(max_length=255, default='NULL')
    HOUR3 = models.CharField(max_length=255, default='NULL')
    HOUR4 = models.CharField(max_length=255, default='NULL')
    HOUR5 = models.CharField(max_length=255, default='NULL')
    HOUR6 = models.CharField(max_length=255, default='NULL')
    HOUR7 = models.CharField(max_length=255, default='NULL')
    HOUR8 = models.CharField(max_length=255, default='NULL')

    def __str__(self):
        return f"{self.STUDENT_ID}"
