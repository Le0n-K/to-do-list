from django import forms
from to_do_list.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline_datetime", "is_done", "tags"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline_datetime", "is_done", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
