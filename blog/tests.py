from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post 1',
            text="This is the desc of post 1",
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user
        )
        cls.post2 = Post.objects.create(
            title='Post 2',
            text='This is desc of post 2',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user
        )

    def test_post_list_url_by_name(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_details_on_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_details_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_details_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_posts_not_shown(self):
        # post 1 is published
        # post 2 is draft
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
