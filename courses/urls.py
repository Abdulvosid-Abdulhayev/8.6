from django.urls import path
from .views import (
    CategoryViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    LessonViewSet,
)
from rest_framework.routers import DefaultRouter


category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

enrollment_list = EnrollmentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
enrollment_detail = EnrollmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

lesson_list = LessonViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
lesson_detail = LessonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('courses', course_list, name='course-list'),
    path('courses/<int:pk>/', course_detail, name='course-detail'),
    path('enrollments/', enrollment_list, name='enrollment-list'),
    path('enrollments/<int:pk>/', enrollment_detail, name='enrollment-detail'),
    path('lessons/', lesson_list, name='lesson-list'),
    path('lessons/<int:pk>/', lesson_detail, name='lesson-detail'),
]
