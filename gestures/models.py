from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Gesture(models.Model):
    GESTURE_LIKE = "L"
    GESTURE_VIEW = "V"
    GESTURE_RETWEET = "R"

    GESTURE_CHOICES = [
        (GESTURE_LIKE, 'Like'),
        (GESTURE_VIEW, 'View'),
        (GESTURE_RETWEET, 'Retweet'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    gestures = models.CharField(max_length=1, choices=GESTURE_CHOICES, default=GESTURE_VIEW)