from rest_framework import serializers
from .models import Post , Comment

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['id','title','text','is_enable','publish_time']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'create_time', 'update_time']