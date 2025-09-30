# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class LegacyAdmin(models.Model):
    login = models.CharField(max_length=24, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=24, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    op = models.CharField(max_length=1)
    name = models.CharField(max_length=128, blank=True, null=True)
    candel = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'admin'

    def __str__(self):
        return self.login


class LegacyArticles(models.Model):
    title = models.CharField(max_length=196)
    date = models.DateField(blank=True, null=True)
    shortdesc = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    contributed = models.CharField(max_length=196)
    # categories = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=1)
    oftheweek = models.CharField(max_length=1, blank=True, null=True)
    offline = models.CharField(max_length=1, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=60, blank=True, null=True)
    item_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'

    def __str__(self):
        return self.title


class LegacyArticlescat(models.Model):
    name = models.CharField(unique=True, max_length=128)
    root = models.CharField(max_length=64, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    lang = models.CharField(max_length=1)
    catdesc = models.TextField(blank=True, null=True)
    csec = models.CharField(max_length=1, blank=True, null=True)
    footer = models.TextField(blank=True, null=True)
    withtitle = models.CharField(max_length=1, blank=True, null=True)
    in_index = models.CharField(max_length=1)
    in_index_root = models.CharField(max_length=64)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=30, blank=True, null=True)
    articles = models.ManyToManyField(LegacyArticles, related_name='categories',
                                      through='LegacyArticlescatArticles')

    class Meta:
        managed = False
        db_table = 'articlescat'

    def __str__(self):
        return self.name


class LegacyArticlescatArticles(models.Model):
    articlescat = models.ForeignKey(LegacyArticlescat, on_delete=models.CASCADE)
    articles = models.ForeignKey(LegacyArticles, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'articlescat_articles'
        unique_together = (('articlescat', 'articles'),)


class LegacyClients(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    login = models.CharField(max_length=24, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=24, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    org = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class LegacyContribs(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    def_field = models.CharField(db_column='def', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'contribs'

    def __str__(self):
        return self.name


class LegacyLinks(models.Model):
    engname = models.CharField(max_length=196)
    hebname = models.CharField(max_length=196)
    url = models.CharField(max_length=255, blank=True, null=True)
    engdesc = models.TextField(blank=True, null=True)
    hebdesc = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    islinks = models.CharField(max_length=1)
    offline = models.CharField(max_length=1, blank=True, null=True)
    hebsite = models.CharField(max_length=1, blank=True, null=True)
    mainsite = models.CharField(max_length=1, blank=True, null=True)
    categories = models.ManyToManyField('LegacyLinkscat',
                                        through='LegacyLinkscatLinks')


    class Meta:
        managed = False
        db_table = 'links'

    def __str__(self):
        return '{} {}'.format(self.engname, self.hebname)


class LegacyLinkscat(models.Model):
    name = models.CharField(unique=True, max_length=128)
    root = models.CharField(max_length=64, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    lang = models.CharField(max_length=1)
    catdesc = models.TextField(blank=True, null=True)
    csec = models.CharField(max_length=1, blank=True, null=True)
    footer = models.TextField(blank=True, null=True)
    in_index = models.CharField(max_length=1)
    in_index_root = models.CharField(max_length=64, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkscat'

    def __str__(self):
        return self.name


class LegacyLinkscatLinks(models.Model):
    linkscat = models.ForeignKey(LegacyLinkscat, on_delete=models.CASCADE)
    links = models.ForeignKey(LegacyLinks, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'linkscat_links'
        unique_together = (('linkscat', 'links'),)


class LegacyLists(models.Model):
    name = models.CharField(unique=True, max_length=128)
    private = models.SmallIntegerField()
    last_sent = models.DateTimeField(blank=True, null=True)
    send_days = models.IntegerField(blank=True, null=True)
    send_count = models.IntegerField(blank=True, null=True)
    news_category = models.CharField(max_length=128)
    last_checked = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists'

    def __str__(self):
        return self.name


class LegacyNews(models.Model):
    title = models.CharField(max_length=196)
    date = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    contributed = models.CharField(max_length=196)
    # categories = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=1)
    offline = models.CharField(max_length=1, blank=True, null=True)
    whatsnew = models.CharField(max_length=1, blank=True, null=True)
    slug = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

    def __str__(self):
        return self.title


class LegacyNewscat(models.Model):
    name = models.CharField(unique=True, max_length=128)
    image = models.CharField(max_length=128, blank=True, null=True)
    lang = models.CharField(max_length=1)
    catdesc = models.TextField(blank=True, null=True)
    bytesdesc = models.IntegerField(blank=True, null=True)
    csec = models.CharField(max_length=1, blank=True, null=True)
    footer = models.TextField(blank=True, null=True)
    root = models.CharField(max_length=64, blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)
    in_index = models.CharField(max_length=1)
    in_index_root = models.CharField(max_length=64, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=30, blank=True, null=True)
    news = models.ManyToManyField(LegacyNews, through='LegacyNewscatNews',
                                  related_name='categories')

    class Meta:
        managed = False
        db_table = 'newscat'

    def __str__(self):
        return self.name


class LegacyNewscatNews(models.Model):
    newscat = models.ForeignKey(LegacyNewscat, on_delete=models.CASCADE)
    news = models.ForeignKey(LegacyNews, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'newscat_news'
        unique_together = (('newscat', 'news'),)


class LegacySubscribers(models.Model):
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=24, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=128, blank=True, null=True)
    opertype = models.CharField(max_length=16, blank=True, null=True)
    opercode = models.CharField(unique=True, max_length=32, blank=True, null=True)
    opercode_date = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()
    words = models.TextField(blank=True, null=True)
    full = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscribers'

    def __str__(self):
        return self.name


class LegacySubscriberslists(models.Model):
    list_id = models.IntegerField()
    subscriber_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscriberslists'
        unique_together = (('list_id', 'subscriber_id'),)
