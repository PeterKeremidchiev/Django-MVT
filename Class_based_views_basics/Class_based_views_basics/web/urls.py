from django.urls import path

from Class_based_views_basics.web.views import IndexRawView, IndexView, TodoListDetailsView, TodoListCreateView

urlpatterns = (
    path('', IndexRawView.as_view(), name='index'),
    path('templateview/', IndexView.as_view(), name='templateview'),
    path("todos/<int:pk>/", TodoListDetailsView.as_view(), name="todo_details"),
    path("todos/create/", TodoListCreateView.as_view(), name="todo_create"),
)