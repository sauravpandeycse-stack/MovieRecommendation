from django.conf.urls import url
from django.urls import include
from Content_Based import views


urlpatterns={
	url('search',views.Searching_Model.Search_Page),
	url('recommend',views.Searching_Model.main_func),
	url('next',views.Searching_Model.Movie_Link),
}