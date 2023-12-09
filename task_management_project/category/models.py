from django.db import models
# from task.models import TaskModel

# Create your models here.
class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=50)
    # task = models.ManyToManyField(TaskModel)
    
    def __str__(self):
        return self.categoryName