from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    ('Physical', 'Physical'),
    ('Language', 'Language'),
    ('Cognitive', 'Cognitive'),
    ('Social', 'Social'),
    ('Nutrition', 'Nutrition'),
    ('Sleep', 'Sleep'),
)

class Milestone(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='milestones')
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('milestone-index')