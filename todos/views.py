import json

from django.shortcuts import render
from django.views import View

from core.helpers import convert_byte_body_to_dict
from todos.forms import TaskForm
from todos.models import Task


class TaskView(View):

    @staticmethod
    def get_queryset():
        return Task.objects.all()

    def get_context(self) -> dict:
        return {
            'tasks': self.get_queryset(),
            'form': TaskForm(),
            'errors': None,
        }

    def return_default_response(self, request):
        return render(
            request,
            'todos/todos_list.html',
            self.get_context()
        )

    def get(self, request):
        return render(request, 'todos/index.html', self.get_context())

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            created_task = form.save(commit=False)
            created_task.save()

            return self.return_default_response(request)

    def delete(self, request):
        body = convert_byte_body_to_dict(request.body)

        task_to_be_deleted = Task.objects.get(id=int(body.get('id')))
        task_to_be_deleted.delete()

        return self.return_default_response(request)

    def put(self, request):
        body = convert_byte_body_to_dict(request.body)

        task_to_be_updated = Task.objects.get(id=int(body.get('id')))

        task_to_be_updated.done = bool(body.get('done'))
        task_to_be_updated.save()

        return self.return_default_response(request)
