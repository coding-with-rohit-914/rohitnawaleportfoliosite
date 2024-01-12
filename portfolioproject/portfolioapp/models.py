from django.db import models

class FeedbackData(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    feedback = models.TextField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Feedback From' + self.name
