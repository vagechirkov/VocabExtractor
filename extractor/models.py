from django.db import models


class Word(models.Model):
    """Words and their properties"""
    word = models.CharField(max_length=100)
    is_known = models.BooleanField(default=False)

    def __str__(self):
        return self.word
