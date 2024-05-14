from django.db import models
from django.contrib.auth.models import User

global LOCATIONS

LOCATIONS = [
    ('공학관', '공학관'),
    ('국제관', '국제관'),
    ('경영관', '경영관'),
    ('도서관', '도서관'),
    ('미래관', '미래관'),
    ('법학관', '법학관'),
    ('북악관', '북악관'),
    ('복지관', '복지관'),
]

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    name = models.CharField(max_length=100) # 공간이름
    location = models.CharField(max_length=10, choices=LOCATIONS) # 위치명
    available_time = models.CharField(max_length=100) # 사용시간
    how_to_use = models.CharField(max_length=200) # 사용방법
    specification = models.TextField() # 특징
    
    class Meta:
        db_table = 'post'
    
    def __str__(self):
        return self.name
    
    def summary(self):
        return self.specification[:100]

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.post.name