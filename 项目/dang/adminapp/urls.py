from django.urls import path
from adminapp import views
app_name='adminapp'
urlpatterns = [
    path('regest/',views.rigster,name='regest'),
    path('create/', views.create, name='create'),
    path('regest_logic/', views.rigster_logic, name='regest_logic'),
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('logout/', views.logout, name='logout'),
    path('checkcaptcha/', views.checkcaptcha, name='checkcaptcha'),
    path('registsucc/',views.registsucc,name='registsucc'),

]