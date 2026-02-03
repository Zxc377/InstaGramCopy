from django.contrib import admin
from .models import Region, Follow, Hashtag, Post, Content, UserProfile, CommentLike, PostLike, Comment
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



@admin.register(Region, Follow, Hashtag,  Content)

class ProductAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CommentInline(TranslationInlineModelAdmin):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    inlines = [CommentInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(CommentLike)
admin.site.register(PostLike)
