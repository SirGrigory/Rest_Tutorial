from django.db import models
from users.models import NewUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image
from io import BytesIO
from django.core.files import File


def upload(instance, filename):
    filename = filename.split('.')[0] 
    return f'posts/{filename}.png'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250,blank=True)
    excerpt = models.TextField(null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    image = models.ImageField(_("Image "), upload_to=upload,default='default.jpg')
    
    objects = models.Manager()  # default manager
    post_objects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)
        
        
    def save(self, *args, **kwargs):

        img = Image.open(self.image.path)
        watermark = Image.open('media/watermark.png').resize((200,200)).convert('RGBA')
        watermark.show()
        img.paste(watermark,(0,0))
        transparent = Image.new('RGBA', img.size, (255,255,255))
        transparent.paste(img, (0,0))
        transparent.paste(watermark, (0,0), mask=watermark)
        buf = BytesIO()
        transparent.save(fp=buf,format ='PNG')
        # transparent.save(self.image.path)
        # transparent.show()
        self.image = File(buf, name='resssssult.png')
        super().save(*args, **kwargs)
        # self.save()
        # img.save(self.image.path)


    def __str__(self):
        return self.title
