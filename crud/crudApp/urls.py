from django.urls import path 
from .views import home, student_edit, student_delete, account_login,account_signup

urlpatterns = [
    path('', account_login, name='account_login'),
    path('signup/', account_signup, name='account_signup'),
    path('home/', home, name='home'),
    path('std/<int:pk>/edit/', student_edit, name='student_edit'),
    path('std/<int:pk>/delete/', student_delete, name='student_delete'),
]
