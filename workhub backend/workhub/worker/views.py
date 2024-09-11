from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Worker
from .serializers import WorkerModSer,WorkerModSerUp

class WorkerViewset(ViewSet):

    def create(self,request,*args,**kwargs):
        ser=WorkerModSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response({"msg":"failed"})
  
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Worker.objects.get(id=id)
        dser=WorkerModSer(ob)
        return Response(dser.data)
  
    def list(self,request,*args,**kwargs):
        ob=Worker.objects.all()
        dser=WorkerModSer(ob,many=True)
        return Response(dser.data)

    def partial_update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Worker.objects.get(id=id)
        ser=WorkerModSerUp(data=request.data,instance=ob)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response({"msg":"failed"})

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Worker.objects.get(id=id)
        ob.delete()
        return Response({"msg":"deleted"})