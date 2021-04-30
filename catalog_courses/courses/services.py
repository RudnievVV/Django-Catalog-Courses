from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from .helpers import (
    courses_search_based_on_dates,
    course_defining,
    course_serializer_validation_ok
    )


def all_courses_defining() -> CourseSerializer:
    courses = Course.objects.all()
    courses_serializer = CourseSerializer(courses, many=True)

    return Response(courses_serializer.data, status=status.HTTP_200_OK)


def add_course_func(data: dict) -> Response:
    course_serializer = CourseSerializer(data=data)

    if course_serializer_validation_ok(course_serializer):
        course_serializer.save()

        return Response(course_serializer.data, status=status.HTTP_201_CREATED)

    return Response(settings.COURSE_FIELDS_CHECK_ERROR, status=status.HTTP_400_BAD_REQUEST)


def course_details_func(course_id: int) -> Response:
    course = course_defining(course_id, Course)
    course_serializer = CourseSerializer(course)

    return Response(course_serializer.data, status=status.HTTP_200_OK)


def course_search_func(data: dict) -> Response:
    title = data.get('title')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if title is not None:
        courses = Course.objects.filter(title__contains=title)
        
        if courses:
            if start_date is not None or end_date is not None:
                courses = courses_search_based_on_dates(courses, start_date, end_date)

        courses_serializer = CourseSerializer(courses, many=True)

        if courses_serializer.data:
            return Response(courses_serializer.data, status=status.HTTP_200_OK)

        return Response(courses_serializer.data, status=status.HTTP_204_NO_CONTENT)

    return Response(settings.COURSE_FIELDS_CHECK_ERROR, status=status.HTTP_400_BAD_REQUEST)


def course_update_func(data: dict) -> Response:
    course = course_defining(data.get('id'), Course)

    if course:
        course_serializer = CourseSerializer(course, data=data)

        if course_serializer_validation_ok(course_serializer):
            course_serializer.save()

            return Response(course_serializer.data, status=status.HTTP_200_OK)

    return Response(settings.COURSE_FIELDS_CHECK_ERROR, status=status.HTTP_400_BAD_REQUEST)


def course_delete_func(data: dict) -> Response:
    course = course_defining(data.get('id'), Course)
    if course:
        course.delete()

        return Response(settings.COURSE_DELETE_SUCCESS.format(course.id), status=status.HTTP_200_OK)

    return Response(settings.COURSE_FIELDS_CHECK_ERROR, status=status.HTTP_400_BAD_REQUEST)