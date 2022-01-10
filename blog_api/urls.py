from django.urls import path
from .views import PostList, PostCreate
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'  # чтоб удобнее прописывать в settings

router = DefaultRouter()
router.register('', PostList, basename='posts')
urlpatterns = router.urls

urlpatterns = [
    path('create/', PostCreate.as_view(), name='post-detail'),
]
