from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('todolist/', views.todolist, name='todolist'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('addtodo/', views.addtodo, name='addtodo'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete-todo'),
    path('change-status/<int:id>/<str:status>', views.change_todo, name='change-todo'),
]
