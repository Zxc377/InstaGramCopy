from .models import Follow, Region, Comment, Post, Hashtag, Content
from modeltranslation.translator import TranslationOptions,register

@register(Follow)
class FavoriteMovie(TranslationOptions):
    fields = ()

@register(Region)
class RegionMovie(TranslationOptions):
    fields = ()

@register(Comment)
class CommentMovie(TranslationOptions):
    fields = ()

@register(Post)
class Post(TranslationOptions):
    fields = ('description',)

@register(Hashtag)
class Hashtag(TranslationOptions):
    fields = ()

@register(Content)
class Content(TranslationOptions):
    fields = ()