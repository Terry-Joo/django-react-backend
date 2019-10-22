from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

SCOPE_CHOICES = (
    ('HIDDEN', '비공개'),
    ('STAFF', '스탭 공개'),
    ('PUBLIC', '전체 공개')
)


class AbstractBasePost(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, editable=False)
    title = models.CharField(unique=False, null=False, blank=False, max_length=50, verbose_name='게시글 이름')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성된 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정된 날짜')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # if not self.pk:
        #     TODO: set uuid
        return super(AbstractBasePost, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                                  update_fields=update_fields)


class AbstractPost(AbstractBasePost):
    writer = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    allow_reply = models.BooleanField(default=False, verbose_name='댓글 허용')
    scope = models.CharField(max_length=40, default=True, verbose_name='공개 범위', choices=SCOPE_CHOICES)

    class Meta:
        abstract = True


class Post(AbstractPost):
    pass
