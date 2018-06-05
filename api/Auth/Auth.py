
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models
from rest_framework.response import Response
class LfAuth(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_param.get("token")
        obj=models.UserAuthToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({"code":1001,"error":"认证失败"})
        else:
            return (obj.user.user,obj)