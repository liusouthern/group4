from rest_framework import serializers

from api.models import *





class Courseializer(serializers.ModelSerializer):
    # 难度级别
    level=serializers.CharField(source="get_level_display")
    #
    sub_category=serializers.CharField(source="sub_category.name")
    hours=serializers.CharField(source="coursedetail.hours")

    category = serializers.CharField(source="sub_category.category.name")
    class Meta:
        model=Course
        fields=["level","id","sub_category","category","brief","hours"]




class CourseDetail(serializers.ModelSerializer):
    level = serializers.CharField(source="course.get_level_display")
    # 课程大类
    sub_category = serializers.CharField(source="course.sub_category.name")
    # 课程子类
    category = serializers.CharField(source="course.sub_category.category.name")
    # 学习周期
    period=serializers.CharField(source="course.period")
    class Meta:
        model=CourseDetail
        fields=["id","level","sub_category","category","hours","course_slogan","video_brief_link",
                "recommend_courses","teacher","period","coursechapter"]

    recommend_courses=serializers.SerializerMethodField()
    def get_recommend_courses(self,obj):
        queryset=obj.recommend_courses.all()
        return [{"id":item.id,"name":item.name}for item in queryset]

    teacher=serializers.SerializerMethodField()
    def get_teacher(self,obj):
        queryset=obj.teachers.all()
        return [{"id":item.id,"name":item.name}for item in queryset]



    # 章节
    coursechapter=serializers.SerializerMethodField()
    def get_coursechapter(self,obj):
        queryset=obj.course.coursechapters.all()
        return [{"name":item.name,"summary":item.summary}for item in queryset]