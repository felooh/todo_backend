from .models import Task

from rest_framework import viewsets,serializers,routers

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']