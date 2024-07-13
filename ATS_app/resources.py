from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import PARENT
from .models import STUDENT
from .models import STUDENT_INFO
from .models import TEACHER
from .models import ATTENDANCE_DATA


class StudentAndInfoResource(resources.ModelResource):
    student_id = fields.Field(attribute='STUDENT_ID', column_name='STUDENT_ID')
    first_name = fields.Field(attribute='FIRST_NAME', column_name='FIRST_NAME')
    last_name = fields.Field(attribute='LAST_NAME', column_name='LAST_NAME')
    parent_id = fields.Field(attribute='PARENT_ID', column_name='PARENT_ID', widget=ForeignKeyWidget(PARENT, 'PARENT_ID'))
    email = fields.Field(attribute='EMAIL_ADDRESS' , column_name='EMAIL_ADDRESS')
    department = fields.Field(attribute='DEPARTMENT', column_name='DEPARTMENT')
    section = fields.Field(attribute='SECTION', column_name='SECTION')

    def before_import_row(self, row, **kwargs):
        student_id = row.get('STUDENT_ID')
        student, created = STUDENT.objects.get_or_create(STUDENT_ID=student_id)
        student.FIRST_NAME = row.get('FIRST_NAME')
        student.LAST_NAME = row.get('LAST_NAME')
        parent_id = row.get('PARENT_ID')

        parent = PARENT.objects.get(PARENT_ID=parent_id)
        student.PARENT_ID = parent
        student.save()
        student_info, created = STUDENT_INFO.objects.get_or_create(STUDENT_ID=student)
        student_info.STUDENT_ID = student
        student_info.DEPARTMENT = row.get('DEPARTMENT')
        student_info.SECTION = row.get('SECTION')
        student_info.save()

    class Meta:
        model = STUDENT
        skip_unchanged = True
        report_skipped = False
        fields = ('student_id', 'first_name', 'last_name', 'parent_id', 'department', 'section')
        import_id_fields = ['student_id']

class PARENTResource(resources.ModelResource):
    class meta:
        model = PARENT

class TEACHERResource(resources.ModelResource):
    class meta:
        model = TEACHER

class ATTENDANCEResource(resources.ModelResource):
    class meta:
        model = ATTENDANCE_DATA