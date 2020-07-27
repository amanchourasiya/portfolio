from django.db import models

# Create your models here.
class PostViews(models.Model):
    blog_id = models.CharField(max_length=100, primary_key=True)
    blog_view_count = models.IntegerField(default=0)
    blog_claps = models.IntegerField(default=0)

    class Meta:
        db_table = 'post_views'
