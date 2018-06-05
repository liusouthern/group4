from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView
from api import models
from api.serializer.course import Courseializer,CourseDetail
from rest_framework.response import Response





class CourseView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        ret={"code":1000}
        try:
            queryset=models.Course.objects.all()
            ser=Courseializer(instance=queryset,many=True)
            ret["data"]=ser.data
        except Exception as e:
            ret["code"]=1001
            ret["error"]="序列化失败"
        return Response(ret)



    def retrieve(self,request,*args,**kwargs):
        ret = {"code": 1000}
        id=kwargs.get("pk")
        try:
            obj = models.CourseDetail.objects.filter(course_id=id).first()
            ser = CourseDetail(instance=obj)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = "序列化失败"
        return Response(ret)