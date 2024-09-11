from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerModSer,CustomerUpSer
# Create your views here.
class CustomerView(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=CustomerModSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response({"msg":"failed"})
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Customer.objects.get(id=id)
        dser=CustomerModSer(ob)
        return Response(dser.data)
    
    def partial_update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Customer.objects.get(id=id)
        ser=CustomerUpSer(data=request.data,instance=ob)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response({"msg":"failed"})
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Customer.objects.get(id=id)
        ob.delete()
        return Response({"msg":"deleted"})