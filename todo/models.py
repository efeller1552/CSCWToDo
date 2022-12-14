import datetime
from django.db import models
from django.conf import settings


class TodoItem(models.Model):
    """
    Todo Item Model
    """    
    name = models.CharField(max_length=100)
    duedate = models.DateField(default=datetime.date.today)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="todo_item")

    class Meta:
        """
        Meta Information
        """
        app_label = "todo"
        db_table = "todo_item"
        verbose_name = "todo_item"
        verbose_name_plural = "todo_items"

    def __str__(self):
        return self.name


class LinkItem(models.Model):
    """
    Link Item Model
    """    
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="link_item")

    class Meta:
        """
        Meta Information
        """
        app_label = "todo"
        db_table = "link_item"
        verbose_name = "link_item"
        verbose_name_plural = "link_items"

    def __str__(self):
        return self.name