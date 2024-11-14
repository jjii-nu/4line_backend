from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    trip_time = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    rating = models.FloatField()
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='community_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # default=timezone.now 제거
    updated_at = models.DateTimeField(auto_now=True)

    # 좋아요 및 스크랩 기능
    likes = models.ManyToManyField(User, related_name="liked_communities", blank=True)
    scraps = models.ManyToManyField(User, related_name="scrapped_communities", blank=True)

    def like_count(self):
        return self.likes.count()

    def scrap_count(self):
        return self.scraps.count()

    def __str__(self):
        return self.title