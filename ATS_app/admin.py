from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import StudentAndInfoResource

from .models import PARENT
from .models import STUDENT
from .models import TEACHER
from .models import STUDENT_INFO
from .models import ATTENDANCE_DATA


# Parent
class PARENTAdmin(ImportExportModelAdmin):
    list_display=('PARENT_ID','FIRST_NAME','LAST_NAME','PHONE_NO','EMAIL_ADDRESS')

admin.site.register(PARENT, PARENTAdmin)

# Student and Student info 
class StudentAndInfoAdmin(ImportExportModelAdmin):
    resource_class = StudentAndInfoResource

admin.site.register(STUDENT, StudentAndInfoAdmin)

# Student info
class STUDENT_INFOAdmin(ImportExportModelAdmin):
    list_display=('STUDENT_ID','DEPARTMENT','SECTION')

admin.site.register(STUDENT_INFO)

# Teacher
class TEACHERAdmin(ImportExportModelAdmin):
    list_display=('TEACHER_ID','PHONE_NO','EMAIL_ADDRESS')

admin.site.register(TEACHER, TEACHERAdmin)

# Attendance
class ATTENDANCEAdmin(ImportExportModelAdmin):
    list_display=('STUDENT_ID','FIRST_NAME','LAST_NAME','DATE','HOUR1','HOUR2','HOUR3','HOUR4','HOUR5','HOUR6','HOUR7','HOUR8')

admin.site.register(ATTENDANCE_DATA, ATTENDANCEAdmin)
