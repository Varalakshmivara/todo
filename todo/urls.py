from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name="addTask"),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('make_as_undo/<int:pk>/',views.make_as_undo,name="make_as_undo"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),
]
