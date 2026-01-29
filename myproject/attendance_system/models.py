from django.db import models
class student(models.Model):
    name = models.CharField(max_length=100)
    roll_no=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name

class attendance(models.Model):
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    class Meta:
        unique_together = ('student','date')

# Create your models here.
