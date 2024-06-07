from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings

from django.views.generic import DetailView
from .models import Category



from .models import Job,Category


# Create your views here.

class YourListView(LoginRequiredMixin,ListView):
    model = Job
    template_name = 'Jobs/Joblist.html'
    context_object_name ='object_list'
    login_url="/login"

class YourDetailView(LoginRequiredMixin,DetailView):
    model = Job  # Replace YourModel with the actual model you're using
    template_name = "Jobs\Jobdetail.html"  # Path to your detail template
    context_object_name = "object"
    login_url="/login"




def Search(request):
   name=request.GET.get("search")
   jobs=Job.cm.all().search(name)
   return render(request,"Jobs/Search.html",{"jobs":jobs})



class CustomSlug(DetailView):
    model = Category
    template_name = 'Category/category.html'
    context_object_name="category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

@method_decorator(staff_member_required,name="dispatch")
class CustomCreateview(LoginRequiredMixin,CreateView):
    model=Job
    fields=["Role","From_Salary","To_Salary","Location", "Company_name","Company_logo","Job_type","Job_description","Company_description"]
    # exclude=["Job_status"]
    template_name="Jobs/Product.html"
    success_url='viewjob' 
    login_url="/login"


class CustomUpdateview(UpdateView):
    model=Job
    fields=["Role","From_Salary","To_Salary","Location", "Company_name","Company_logo","Job_type","Job_description","Company_description"]
    template_name="Jobs/Product.html"
    success_url='/Job/viewjob'

class CustomremoveView(DeleteView):
    model=Job   
    success_url='/Job/viewjob'
    template_name="Jobs/confirm_delete.html"
    



@method_decorator(staff_member_required, name='dispatch')
class CustomAdminView(ListView):
    model = Job
    template_name = "Jobs/Admin.html"
    context_object_name = "object"
    login_url = "/login"





def apply_job(request,job_id):
    message="none"
    if request.method == 'POST': 
             setJob= get_object_or_404(Job,id=job_id)
             setJob.Job_status=True
             setJob.user=request.user
             setJob.save()
         
             subject = 'Applying Job'
             message = f"Thankyou for Applying Job at {setJob.Company_name}"
             reciept=request.user.email
             send_mail(subject, message, 'Chandanmani118@gmail.com',[reciept,])
    return render(request,"Jobs/apply_job.html",{"message":message})


def Applied_Job(request):
    # Assuming Job.cm is a custom manager filtering applied jobs based on user and job status
    objects = Job.cm.filter(user=request.user, Job_status=True)
    return render(request, "Jobs/AppliedJob.html", {"objects": objects})
    




