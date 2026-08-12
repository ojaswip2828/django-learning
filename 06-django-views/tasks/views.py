from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def home(request):
    return HttpResponse("Welcome to the Django Views Project!")


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "tasks/task_detail.html", {"task": task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")

    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list_cbv.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail_cbv.html"
    context_object_name = "task" 
    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form_cbv.html"
    success_url = "/cbv/tasks/"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form_cbv.html"
    success_url = "/cbv/tasks/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete_cbv.html"
    success_url = "/cbv/tasks/"