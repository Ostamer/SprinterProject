# from django.db import models
#
# class NewsPlate(models.Model):
#     author_id = models.ForeignKey('Author', on_delete=models.CASCADE)
#     comments_id = models.ForeignKey('Comments', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     text = models.CharField()
#     image_src = models.ImageField(upload_to='news_images/', null=True, blank=True)
#     likes_count = models.BigIntegerField()
#     create_date = models.DateField()
