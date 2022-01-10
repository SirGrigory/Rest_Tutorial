from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='testcategory')
        tetst_user_1 = User.objects.create(
            username='testuser', password='123456789')
        test_post_1 = Post.objects.create(
            title='testtitle', category_id=1, excerpt='testexcerpt', content='testcontent', slug='post-tt', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.post_objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'testtitle')
        self.assertEqual(excerpt, 'testexcerpt')
        self.assertEqual(content, 'testcontent')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'testtitle')
        self.assertEqual(str(cat), 'testcategory')
