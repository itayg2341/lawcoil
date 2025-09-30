from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField
from django.urls import reverse

from law.content.models import Article, NewsItem, ComputerLaw


class KnowledgeCenter(models.Model):
    name = models.CharField(_('Name'), max_length=200, unique=True)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    description = RichTextField(_('Description'))
    photo = models.ImageField(
        _('Large Photo'), blank=True, null=True,
        help_text=_('Preferably at size of 1168x370'))
    small_photo = models.ImageField(
        _('Small Photo'), blank=True, null=True,
        help_text=_('Preferably at size of 583x177'))
    order = models.IntegerField(_('Order'), default=0, db_index=True)

    class Meta:
        verbose_name = _('Knowledge Center')
        verbose_name_plural = _('Knowledge Centers')
        ordering = ('order', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('knowledge:detail', kwargs={'slug': self.slug})


class KnowledgeCenterItem(models.Model):
    knowledge_center = models.ForeignKey(
        KnowledgeCenter, verbose_name=_('Knowledge Center'),
        related_name='items',
        on_delete=models.CASCADE
    )

    title = models.CharField(
        _('Title'), max_length=200, blank=True, null=True,
        help_text=_('In case of article, news or computer law, '
                    'leave this blank'))
    slug = models.SlugField(
        _('Slug'), max_length=100, blank=True, null=True,
        help_text=_('In case of article, news or computer law, '
                    'leave this blank'))
    display_in_listing = models.BooleanField(_('Display in listing'),
                                             default=True,)
    order = models.IntegerField(_('Order'), default=0, db_index=True)
    content = RichTextField(
        _('Content'), blank=True, null=True,
        help_text=_('In case of article, news or computer law, '
                    'leave this blank'))

    article = models.ForeignKey(
        Article, verbose_name=_('Article'),
        related_name='knowledge_center_articles',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    news_item = models.ForeignKey(
        NewsItem, verbose_name=_('News Item'),
        related_name='knowledge_center_news',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    computer_law = models.ForeignKey(
        ComputerLaw, verbose_name=_('Computer Law'),
        related_name='knowledge_center_computer_laws',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    url = models.URLField(_('Link to'), max_length=255, blank=True, null=True)

    attachment = models.FileField(
        _('Attached file'), upload_to='knowledge-centers',
        max_length=255, blank=True, null=True)

    video = EmbedVideoField(
        _('Embedded Video'), blank=True, null=True,
        help_text=_('Video link from YouTube or Vimeo'))

    class Meta:
        verbose_name = _('Knowledge Center Item')
        verbose_name_plural = _('Knowledge Center Items')
        index_together = [
            ['order', 'display_in_listing']
        ]

    def __str__(self):
        return self.title

    @property
    def content_item(self):
        return self.article or self.news_item or self.computer_law

    def type_description(self):

        if self.article:
            return _('Article')

        if self.news_item:
            return _('News Item')

        if self.computer_law:
            return _('Computer Law')

        if self.url:
            return _('Link')

        if self.attachment:
            return _('Document')

        if self.video:
            return _('Video')

        return _('Content')
    type_description.short_description = _('Item type')

    def get_absolute_url(self):

        if self.content_item:
            return self.content_item.get_absolute_url()

        kwargs = {
            'knowledge_slug': self.knowledge_center.slug,
            'slug': self.slug,
        }
        return reverse('knowledge:item', kwargs=kwargs)

    def computed_title(self):
        content_item = self.content_item
        return content_item.title if content_item else self.title
    computed_title.short_description = _('Title')

    @property
    def computed_content(self):
        content_item = self.content_item
        return content_item.content if content_item else self.content

    def clean(self):
        super().clean()
        if not self.content_item and not all([self.title, self.content,
                                              self.slug]):
            raise ValidationError(_('Title, Content and Slug are required '
                                    'when not article, news item or verdict'))
