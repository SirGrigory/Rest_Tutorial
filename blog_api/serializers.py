from rest_framework import serializers
from blog.models import Post



class PostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author','image','category', 'excerpt', 'content', 'status')
        


