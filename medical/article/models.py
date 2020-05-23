import uuid
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from medical.utils.models import CreatedUpdatedMixin

from taggit.managers import TaggableManager


def upload_main_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex.__str__()}.{ext}'
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    return f"article/main_images/{year}/{month}/{day}/{new_filename}"



class Category(CreatedUpdatedMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名', help_text='分类名')
    nums = models.IntegerField(default=0, verbose_name='分类文章数', help_text='分类文章数')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleQuerySet(models.query.QuerySet):

    def get_counted_tags(self, queryset):
        tag_dict = {}
        query = queryset.annotate(tagged=models.Count('tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1
                else:
                    tag_dict[tag] += 1
        return tag_dict.items()


class Article(CreatedUpdatedMixin, models.Model):
    title = models.CharField(max_length=100, verbose_name='标题', help_text='文章标题')
    category = models.ForeignKey(Category ,on_delete=models.CASCADE, verbose_name='分类', help_text='文章分类')
    main_image = models.ImageField(upload_to=upload_main_image, verbose_name="主图", null=True, blank=True)
    content = RichTextUploadingField(verbose_name="活动描述", null=True, blank=True)
    comment_nums = models.IntegerField(default=0, verbose_name='评论数', help_text='评论数')
    read_nums = models.IntegerField(default=0, verbose_name='阅读数', help_text='阅读数')

    tags = TaggableManager()

    objects = ArticleQuerySet.as_manager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
