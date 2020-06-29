from rest_framework import serializers
from app2.models import Student
from drf_proj import settings

class StudentSerializer(serializers.Serializer):
    stuname = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()

    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):

        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


class StudentDeSerializer(serializers.Serializer):
    stuname = serializers.CharField(
        max_length=8,
        min_length=4,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
