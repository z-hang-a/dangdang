from django.urls import path
from carapp import views
app_name='carapp'
urlpatterns = [
    path('shpping/',views.car,name='car'),
    path('addshpping/',views.add_car,name='addcar'),
    path('delshpping/',views.del_car,name='delcar'),
    path('change/', views.change, name='changecar'),
    path('recover/',views.recover_item,name='recover'),
    path('indent/', views.indent, name='indent'),
    path('indent_logic/', views.indent_logic, name='indent_logic'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
    path('old_address/', views.old_address, name='old_address'),

]