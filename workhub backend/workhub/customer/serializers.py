from rest_framework.serializers import ModelSerializer
from .models import Customer

class CustomerModSer(ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"
    
class CustomerUpSer(ModelSerializer):
    class Meta:
        model=Customer
        exclude=('profilepic')