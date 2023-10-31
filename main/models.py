from django.db import models
from uuid import uuid4


class DataType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class FlaggedData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data_type = models.ForeignKey('DataType', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, unique=True)
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.value
