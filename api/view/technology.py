
from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView
from api import models
from api.serializer.technology import  TechnologySerializer,TechnologyDetailSerializer
from rest_framework.response import Response
class TechnologyView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        res={"code":1000}

        try:
            queryset = models.ArticleSource.objects.all()
            ser=TechnologySerializer(instance=queryset,many=True)
            res["data"]=ser.data
        except Exception as e:
            res["code"]=1001
            res["error"]="序列化失败"
        return Response(res)


    def create(self,request,*args,**kwargs):
        pass

    def retrieve(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        res = {"code": 1000}
        try:
            obj = models.Article.objects.filter(source_id=pk).first()
            ser=TechnologyDetailSerializer(instance=obj,many=False)
            res["data"] = ser.data
        except Exception as e:
            res["code"]="1001"
            res["error"]="序列化失败"
            print(e)
        return Response(res)