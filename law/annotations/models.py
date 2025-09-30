
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from law.content.models import CommonContent
from law.users.models import User


class Annotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name=_('User'),
                             related_name='annotations',
                             on_delete=models.CASCADE)
    content = models.ForeignKey(CommonContent, verbose_name=_('Content'),
                                related_name='annotations',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    annotation_object = models.JSONField(_('Annotation object'), default=dict)

    class Meta:
        index_together = ['user', 'content']
        verbose_name = _('Annotation')
        verbose_name_plural = _('Annotations')
