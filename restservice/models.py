# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FrontpageStats(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    useragent = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    pageviews = models.PositiveIntegerField()
    jscr0 = models.PositiveIntegerField()
    jscr1 = models.PositiveIntegerField()
    cook0 = models.PositiveIntegerField()
    cook1 = models.PositiveIntegerField()
    ajax0 = models.PositiveIntegerField()
    ajax1 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'frontpage_stats'


class GeneAutocomplete(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    species = models.CharField(max_length=255, blank=True, null=True)
    stable_id = models.CharField(max_length=128, primary_key=True)
    display_label = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    db = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'gene_autocomplete'


class HelpLink(models.Model):
    help_link_id = models.AutoField(primary_key=True)
    page_url = models.TextField(blank=True, null=True)
    help_record_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_link'


class HelpRecord(models.Model):
    help_record_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    keyword = models.TextField(blank=True, null=True)
    data = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    helpful = models.IntegerField(blank=True, null=True)
    not_helpful = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_record'