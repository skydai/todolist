from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from task.models import Task
from api.serializers import TaskSerializer

class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(TaskMixin, ListCreateAPIView):
    pass

    # return task ,creating a new


class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    pass

    # return , upfate , delete
