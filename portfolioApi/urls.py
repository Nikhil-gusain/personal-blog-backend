from django.urls import path,include
from . import views

urlpatterns = [
    path('about/',views.GetAboutSectionView,name='about'),
    path('services/',views.GetServiceSectionView,name='services'),
    path('blog/',views.GetBlogsforApiView,name='blogsApi'),
    path('skills/',views.GetSkillSectionView,name='skills'),
    path('contact/',views.GetContactSectionView,name='contact'),
]
