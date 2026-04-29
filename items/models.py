from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class ItemPost(models.Model):
    TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    title = models.CharField(max_length=100)
    post_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='items/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    claimed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} ({self.post_type})"