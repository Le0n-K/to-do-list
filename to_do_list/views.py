from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from to_do_list.models import Task, Tag
from to_do_list.forms import TaskCreationForm, TaskUpdateForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_list/task_confirm_delete.html"
    success_url = reverse_lazy("to_do_list:task-list")


def toggle_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("to_do_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = 'to_do_list/tag_list.html'
    context_object_name = 'tags'


# Create view for Tag
class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'to_do_list/tag_form.html'
    success_url = reverse_lazy('to_do_list:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'to_do_list/tag_form.html'
    success_url = reverse_lazy('to_do_list:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'to_do_list/tag_confirm_delete.html'
    success_url = reverse_lazy('to_do_list:tag-list')


# from django.urls import reverse_lazy
# from django.views import generic
#
# from to_do_list.forms import TaskCreationForm, TaskUpdateForm
# from to_do_list.models import Task
#
#
# class TaskListView(generic.ListView):
#     model = Task
#     template_name = "to_do_list/task_list.html"
#     context_object_name = "tasks"
#
#
# class TagListView(generic.ListView):
#     model = Task
#     template_name = "to_do_list/tag_list.html"
#     context_object_name = "tag"
#
#
# class TaskCreateView(generic.CreateView):
#     model = Task
#     template_name = "to_do_list/task_create.html"
#     success_url = reverse_lazy("to_do_list:task-list")
#     form_class = TaskCreationForm
#
#
# class TaskDeleteView(generic.DeleteView):
#     model = Task
#     template_name = "to_do_list/task_delete.html"
#     success_url = reverse_lazy("to_do_list:task-list")
#
#
# class TaskUpdateView(generic.UpdateView):
#     model = Task
#     success_url = reverse_lazy("to_do_list:task-list")
#     form_class = TaskUpdateForm
