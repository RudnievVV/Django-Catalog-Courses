from django.urls import path
from . import views

urlpatterns = [
    path('courses-all/', views.all_courses),
    path("course-add", views.course_add),
    path("course/<int:course_id>/", views.course_details),
    path("course-search/", views.course_search),
    path("course-update", views.course_update),
    path("course-delete", views.course_delete),
]