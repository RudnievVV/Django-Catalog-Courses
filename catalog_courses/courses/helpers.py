from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import datetime


def course_fields_ok(start_date: datetime, end_date: datetime, lectures_qty: int) -> bool:
    if start_date is not None and end_date is not None and str(lectures_qty).isdigit():
        if end_date >= start_date:
            return True

    return False


def convert_str_to_date(date: str) -> datetime:
    """date string must be in format YYYY-MM-DD"""
    if date is not None:
        date_list = date.split('-')
        
        if len(date_list) == 3 and date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
            try:
                date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))

                return date
            except Exception:
                pass

        return None


def courses_search_based_on_dates(courses: list, start_date: str, end_date: str) -> list:
    start_date = convert_str_to_date(start_date)
    end_date = convert_str_to_date(end_date)

    if start_date is not None and end_date is not None:
        return courses.filter(Q(start_date__gte=start_date), Q(end_date__lte=end_date))

    if start_date is not None and end_date is None:
        return courses.filter(start_date__gte=start_date)

    if start_date is None and end_date is not None:
        return courses.filter(end_date__lte=end_date)

    

def course_defining(course_id: int, Course: object) -> object:
    if str(course_id).isdigit():
        return get_object_or_404(Course, pk=course_id)

    return False


def course_serializer_validation_ok(course_serializer: object) -> bool:
    if course_serializer.is_valid() and course_fields_ok(course_serializer.validated_data.get('start_date'),
                                                        course_serializer.validated_data.get('end_date'),
                                                        course_serializer.validated_data.get('lectures_qty')):
        return True
    
    return False