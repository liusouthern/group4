from rest_framework import serializers
from api .models import *
import datetime

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleSource
        fields="__all__"

class TechnologyDetailSerializer(serializers.ModelSerializer):



    class Meta:
        model=Article
        fields=["id","title","view_num","collect_num","comment_num","brief","date","pub_date","offline_date","content"]

    date = serializers.SerializerMethodField()
    def get_date(self,obj):
        time2=obj.date
        time2=time2.strftime("%Y-%m-%d %H:%M:%S")
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d1=datetime.datetime.strptime(time2,"%Y-%m-%d %H:%M:%S")
        d2=datetime.datetime.strptime(now,"%Y-%m-%d %H:%M:%S")
        day=(d2-d1).days
        if int(day)>7:
            week,more=divmod(int(day), 7)
            return str(week)+"周前创建"
        return str(day)+"天前创建"

    pub_date=serializers.SerializerMethodField()
    def get_pub_date(self,obj):
        time=obj.pub_date
        time=time.strftime("%Y-%m-%d %H:%M:%S")
        return time

    offline_date = serializers.SerializerMethodField()

    def get_offline_date(self, obj):
        time = obj.offline_date
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        return time