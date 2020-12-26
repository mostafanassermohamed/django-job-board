from django.db import models

# Create your models he
 
JOB_TYPE=( 

    ('full time','full time'),
    ('part time','part time'),
    

)

class Job(models.Model):        #table
    title=models.CharField(max_length=100)
    #location= 
    #category=models.ForeignKey('Category',on_delete=models.CASCADE)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE )
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    sallary=models.IntegerField(default=0)
    experience=models.IntegerField(default=0)


    def __str__(self):
        return self.title     