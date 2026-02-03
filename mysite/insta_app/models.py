from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user_image = models.ImageField(upload_to='users/', null=True, blank=True)
    user_link = models.URLField(null=True, blank=True)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile,related_name='followers',on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile,related_name='following',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} → {self.following}'



class Region(models.Model):
    region_name = models.CharField(max_length=20, null=True, blank=True)


class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=99, null=True, blank=True)


class Post(models.Model):
    author = models.ForeignKey(UserProfile, related_name='author', on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    hashtag = models.ManyToManyField(Hashtag, blank=True)
    music = models.FileField(null=True, blank=True)
    people = models.ManyToManyField(UserProfile, related_name='tagged_in_posts', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Content(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField()
