from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('items', views.TodoListApiView.as_view()),
    path('items/<int:item_id>', views.TodoListApiView.as_view()),
]