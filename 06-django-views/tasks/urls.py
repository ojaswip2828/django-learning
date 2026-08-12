from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # FBV
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:task_id>/edit/", views.task_update, name="task_update"),
    path(
        "tasks/<int:task_id>/delete/",
        views.task_delete,
        name="task_delete",
    ),

    # CBV
    path(
        "cbv/tasks/",
        views.TaskListView.as_view(),
        name="cbv_task_list",
    ),

    path(
        "cbv/tasks/<int:pk>/",
        views.TaskDetailView.as_view(),
        name="cbv_task_detail",
    ),

    path(
        "cbv/tasks/create/",
        views.TaskCreateView.as_view(),
        name="cbv_task_create",
    ),

    path(
        "cbv/tasks/<int:pk>/edit/",
        views.TaskUpdateView.as_view(),
        name="cbv_task_update",
    ),

    path(
        "cbv/tasks/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="cbv_task_delete",
    ),
]