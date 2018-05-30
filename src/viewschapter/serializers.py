from rest_framework import serializers
from posts import models


class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()

    def get_posted_by(self, obj):
        return obj.posted_by.username

    class Meta:
        model = models.Post
        fields = ("posted_by", "message",)
