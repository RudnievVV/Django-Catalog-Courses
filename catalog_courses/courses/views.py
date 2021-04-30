from rest_framework.decorators import api_view
from .services import (
    all_courses_defining,
    add_course_func,
    course_details_func,
    course_search_func,
    course_update_func,
    course_delete_func
    )


@api_view(["GET"])
def all_courses(request):
    response = all_courses_defining()

    return response


@api_view(["POST"])
def course_add(request):
    response = add_course_func(request.data)

    return response


@api_view(["GET"])
def course_details(request, course_id):
    response = course_details_func(course_id)

    return response


@api_view(["GET"])
def course_search(request):
    response = course_search_func(request.GET)

    return response


@api_view(["PUT"])
def course_update(request):
    response = course_update_func(request.data)

    return response


@api_view(["Delete"])
def course_delete(request):
    response = course_delete_func(request.data)
    
    return response