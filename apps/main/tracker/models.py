from django.db import models

SHAPE_CHOICES = [
    ('triangle', 'Triangle'),
    ('square', 'Square'),
    ('circle', 'Circle'),
]

COLOR_CHOICES = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
]

class Entry(models.Model):
    name = models.CharField(max_length=255)
    shape = models.CharField(max_length=100, choices=SHAPE_CHOICES)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Ensures latest entries appear first