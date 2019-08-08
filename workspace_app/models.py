import datetime
from datetime import timedelta
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    HIGH_SCHOOL = 'HI'
    COLLEGE = 'CO'
    UNIVERSITY = 'UN'
    MASTERS = 'MA'
    PHD = 'PH'
    OTHERS = 'OT'

    ACADEMIC_LEVEL_CHOICES = [
                    (HIGH_SCHOOL, 'High School'),
                    (COLLEGE, 'College'),
                    (UNIVERSITY, 'University'),
                    (MASTERS, 'Masters'),
                    (PHD, 'PHD'),
                    (OTHERS, 'Others'),
        ]

    ENGLISH_UK = 'ENGUK'
    ENGLISH = 'ENGUS'

    LANGUAGE_CHOICES = [(ENGLISH_UK,'English(U.K)'),
                        (ENGLISH, 'English'),]

    UNASSIGNED = 'UA'
    ASSIGNED ='AS'
    REVISION = 'RE'
    COMPLETED ='CO'
    CANCELLED = 'CA'
    ON_HOLD = 'OH'
    TEST = 'TE'
    INQUIRY = 'IQ'

    TASK_STATUS_CHOICES = [(UNASSIGNED,'Not Assigned'),
                            (ASSIGNED, 'Assigned'),
                            (REVISION,'On Revision'),
                            (COMPLETED,'Completed'),
                            (CANCELLED,'Cancelled'),
                            (ON_HOLD, 'On hold'),
                            (TEST,'Test Task'),
                            (INQUIRY, 'Inquiry'),]

    task_number = models.CharField(max_length = 15, unique = True)
    topic = models.CharField(max_length = 100)
    pages = models.SmallIntegerField()
    single_spaced = models.BooleanField("single spaced",default = False)
    slides = models.SmallIntegerField()
    style = models.CharField(max_length = 10)
    date_due = models.DateTimeField()
    task_cost = models.DecimalField(max_digits = 5, decimal_places = 2)
    task_cpp = models.FloatField()
    task_academic_level = models.CharField(max_length = 2, choices = ACADEMIC_LEVEL_CHOICES,)
    sources = models.SmallIntegerField()
    task_type = models.CharField(max_length = 15)
    subject = models.CharField (max_length = 20)
    language = models.CharField(max_length = 5, choices = LANGUAGE_CHOICES,)
    task_status = models.CharField(max_length= 2, choices = TASK_STATUS_CHOICES,)
    description = models.TextField()
    #task_documents = models.FileField(upload_to ='uploaded_documents/', null = True)
    comments = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.task_number


class TaskFile(models.Model):
    file = models.FileField(upload_to = 'uploaded_documents/')
    task = models.ForeignKey(Task, on_delete = models.CASCADE, related_name='files')

class Writer(models.Model):
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=100)
    telephone = models.PositiveIntegerField()
    alternate_telephone = models.PositiveIntegerField( blank = True)
    registration_date = models.DateTimeField(default=timezone.now)

    ACTIVE = 'AC'
    SUSPENDED = 'SU'
    PROBATION = 'PR'
    NOTACTIVE = 'NA'

    STATUS_CHOICES = [(ACTIVE,'Active'),
                      (SUSPENDED, 'Suspended'),
                      (PROBATION, 'Probation'),
                      (NOTACTIVE,'Inactive'),]
    status=models.CharField(max_length = 10, choices = STATUS_CHOICES, default = ACTIVE)
    academic_level = models.CharField(max_length = 30, choices = Task.ACADEMIC_LEVEL_CHOICES, default = Task.UNIVERSITY)
    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)
