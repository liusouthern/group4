
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
import uuid
class LoginView(APIView):

    def post(self,request,*args,**kwargs):
        res = {"code": 1000}
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user=models.Account.objects.filter(username=user,password=pwd).first()
        if user:
            uid=uuid.uuid4()

        else:
            res["error"]="用户名密码错误"
            return Response(res)