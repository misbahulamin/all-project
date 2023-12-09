from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskCategory = models.ManyToManyField(CategoryModel)
    taskDescreption = models.TextField()
    isCompleted = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField()
    
    def __str__(self):
        return self.taskTitle
    