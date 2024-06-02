# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Commentary(models.Model):
    comm_id = models.UUIDField(primary_key=True)
    comm_text = models.CharField()
    create_date = models.DateTimeField()
    parent_comm = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('SpUser', models.DO_NOTHING)
    post = models.ForeignKey('Post', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'commentary'


class Post(models.Model):
    post_id = models.UUIDField(primary_key=True)
    title = models.CharField()
    small_text = models.CharField()
    full_text = models.CharField()
    image_src = models.CharField()
    create_date = models.DateTimeField()
    user = models.ForeignKey('SpUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post'


class PostTag(models.Model):
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_tag'


class SpUser(models.Model):
    user_id = models.UUIDField(primary_key=True)
    last_name = models.CharField()
    first_name = models.CharField()
    middle_name = models.CharField(blank=True, null=True)
    login = models.CharField(blank=True, null=True)
    user_password = models.CharField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_user'


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True)
    tag_text = models.CharField()

    class Meta:
        managed = False
        db_table = 'tag'
