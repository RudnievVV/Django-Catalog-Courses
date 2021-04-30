from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from .helpers import course_fields_ok


class Course(models.Model):
    title = models.CharField(max_length=settings.COURSE_TITLE_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    lectures_qty = models.PositiveIntegerField(default=settings.COURSE_DEFAULT_LECTURES_QTY)


    # needed if admin will decide to add course through django admin
    def clean(self):
        if not course_fields_ok(self.start_date, self.end_date, self.lectures_qty):
            raise ValidationError(settings.COURSE_FIELDS_CHECK_ERROR)
    
    def __str__(self):
        return self.title