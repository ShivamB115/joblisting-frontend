from django.db import models

class api_job(models.Model):  
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField()

    class Meta:
        db_table = 'api_job'  

    def __str__(self):
        return self.title
