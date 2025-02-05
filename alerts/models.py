from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

current_time = int(datetime.now().timestamp())
# The validate_severity function is placed in the model to 
# ensure that the validation logic is enforced at the database level,
#  regardless of how the data is being created or modified
def validate_severity(value):
    if value not in ['low', 'medium', 'high', 'critical']:
        raise ValidationError(f'{value} is not a valid severity')
def validate_status(value):
    if value not in ['open', 'closed']:
        raise ValidationError(f'{value} is not a valid status')


# Create your models here.
class alerts(models.Model):
    _id = models.AutoField(primary_key=True)
    alert_id = models.CharField(max_length=200, unique=True , null=False, blank=False  )
    severity = models.CharField(max_length=100, validators=[validate_severity])
    description = models.CharField(max_length=1000)
    short_description = models.CharField(max_length=100)
    src = models.CharField(max_length=100)
    dst = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created = models.BigIntegerField(default=current_time)
    updated = models.BigIntegerField(default=current_time)
    json_data = models.JSONField(default=dict)
    source = models.CharField(max_length=100)
    status = models.CharField(max_length=5,default="open")


class IAMRoles(models.Model):
    _id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100, unique=True)
    created = models.BigIntegerField(default=current_time)
    updated = models.BigIntegerField(default=current_time)

class IAMUsers(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    created = models.BigIntegerField(default=current_time)
    updated = models.BigIntegerField(default=current_time)
    role = models.ForeignKey(IAMRoles, on_delete=models.CASCADE)  
    REQUIRED_FIELDS = ['username', 'email', 'role',"password"]
    USERNAME_FIELD = 'username'
    

