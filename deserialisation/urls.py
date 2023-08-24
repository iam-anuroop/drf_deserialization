from django.contrib import admin
from django.urls import path
from dese import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stucre/', views.student_createview),
]
