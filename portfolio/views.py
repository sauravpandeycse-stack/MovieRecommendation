from django.shortcuts import render

# Create your views here.
def PortfolioPage(request):
	res=render(request,'index.html')
	return res

def insertFriendData(request):
	print("friend form data")