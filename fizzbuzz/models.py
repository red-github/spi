from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    createdby = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
        db_table = 'categories'



class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='to_my_parent',
        on_delete=models.PROTECT
    )
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
        db_table = 'sub_categories'