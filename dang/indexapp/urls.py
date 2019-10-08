from django.urls import path
from indexapp import views
app_name='bookapp'
urlpatterns = [
    path('index/',views.index_show,name='index'),
    path('booklist/',views.book_list,name='booklist'),
    path('bookdetails/',views.bookdetails,name='bookdetails'),
]