from rest_framework.serializers import ModelSerializer
from .models import Worker

class WorkerModSer(ModelSerializer):
    class Meta:
        model=Worker
        fields="__all__"

class WorkerModSerUp(ModelSerializer):
    class Meta:
        model=Worker
        exclude=('profilepic',)