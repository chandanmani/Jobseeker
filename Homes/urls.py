
from django.urls import path
from .views import YourListView,YourDetailView,Search,CustomSlug,CustomCreateview,CustomUpdateview,CustomremoveView,CustomAdminView,apply_job,Applied_Job
urlpatterns = [
    path('Job/viewjob',YourListView.as_view(), name='Job'), 
      path('Job/<int:pk>/', YourDetailView.as_view(), name='detail'),
       path('Job/Search',Search,name="Search"),
       path('Category/<slug:slug>',CustomSlug.as_view(),name="CustomSlug"),
       path('Job/PostJob',CustomCreateview.as_view(),name="PostJob"),
       path('Job/UpdateJob/<int:pk>/',CustomUpdateview.as_view(),name="UpdateJob"),
       path('Job/DeleteJob/<int:pk>/',CustomremoveView.as_view(),name="RemoveJob"),
       path("Job/Adminview",CustomAdminView.as_view(),name="Adminview"),
       path('Job/applyjob<int:job_id>',apply_job,name="Set"),
       path('Job/AppliedJob',Applied_Job,name="New")
     
         # URL for the home page
    # Add more URL patterns as needed
]
  