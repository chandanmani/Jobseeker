from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class CustomQuerySet(models.QuerySet):
    def search(self, value):
        return self.filter(Role__icontains=value)

class CustomerManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model)
    
class Category(models.Model):
    # category = models.ForeignKey(Job, on_delete=models.CASCADE)  # Assuming Job is another model
    category_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="category_name", unique=True) 

    def __str__(self):
        return f"{self.slug}"
    


    

class Job(models.Model):
    Role = models.CharField(max_length=30)
    From_Salary = models.IntegerField(default=10)
    To_Salary = models.IntegerField(default=20)
    Location = models.CharField(max_length=30)
    Company_name = models.CharField(max_length=30)
    Company_logo = models.ImageField(upload_to='./Homes/', default="NONE")
    Job_type = models.CharField(max_length=50, default="Full Time")
    category=models.ForeignKey(Category,null=True,on_delete=models.PROTECT)
    Job_description=models.TextField(default="Job Description",null=True)
    Company_description=models.TextField(default="Company Description",null=True)
    Job_status=models.BooleanField(default=False)
    cm = CustomerManager()
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    

    def __str__(self):
        return f" {self.id} {self.Role} "


