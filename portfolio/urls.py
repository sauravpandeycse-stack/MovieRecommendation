from django.conf.urls import url
from django.urls import include
from portfolio import views


urlpatterns={
	url('myprofile',views.PortfolioPage),
	url('insertfriend',views.insertFriendData)
	
}