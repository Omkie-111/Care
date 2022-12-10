from django.db import models
import uuid


# for base using uuid as primary key  and we will use it in our main project

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    #created_at = models.DateTimeField()
    #updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True