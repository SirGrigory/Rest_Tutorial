from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions, BasePermission, SAFE_METHODS ,AllowAny


class PostUserWritePermission(BasePermission):
    message = 'Editing post is to author'

    def has_object_permission(self, request, view, obj): 
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    # queryset = Post.post_objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, title=item)

    def get_queryset(self):
        return Post.objects.all()


class PostCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    






# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.post_objects.all()

#     def list(self,request):
#         serializer_class = PostSerializer(self.queryset,many= True)
#         return Response(serializer_class.data)

#     def retrieve(self,request, pk=None):
#         post = get_object_or_404(self.queryset,pk =pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissions]
#     queryset = Post.post_objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
