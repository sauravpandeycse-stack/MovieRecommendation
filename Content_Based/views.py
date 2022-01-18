from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.


class Searching_Model:
	user_enterd_movie=''
	movie_list=[]
	def Search_Page(request):
		res=render(request,'search_page.html')
		return res
	def main_func(request):
		df=pd.read_csv("C:\\Users\\saura\\Downloads\\movie_dataset.csv")
		df["keywords"]=df["keywords"].str.lower()
		df["cast"]=df["cast"].str.lower()
		df["genres"]=df["genres"].str.lower()
		df["director"]=df["director"].str.lower()
		df["title"]=df["title"].str.lower()
		features=['keywords','cast','genres','director']
		for feature in features:
			df[feature]=df[feature].fillna('')

		def combine_features(row):
			return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']

		df['combine_features']=df.apply(combine_features,axis=1)
		cv=CountVectorizer()
		count_matrix=cv.fit_transform(df["combine_features"])
		cs=cosine_similarity(count_matrix)
		movie_user_likes =request.POST['search']
		movie_user_likes=movie_user_likes.lower()
		user_enterd_movie=movie_user_likes.lower()
		def get_index_from_title(title):
			return df[df.title == title]["index"].values[0]

		movie_index=get_index_from_title(movie_user_likes)
		similar_movies=list(enumerate(cs[movie_index]))
		sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)

		def get_title_from_index(index):
			return df[df.index == index]["title"].values[0]

		i=0
		disp_list=[]
		
		for movie in sorted_similar_movies:
			disp_list.append(get_title_from_index(movie[0]))
			i=i+1
			if i>5:
				break
		res=render(request,'search_page.html',{'movie_data':disp_list})
		return res


	def Movie_Link(request):
		df=pd.read_csv("C:\\Users\\saura\\Downloads\\movie_dataset.csv")
		m_title=request.GET['m_title']
		for i in range(0,len(df)):
  		  if df.iloc[i][18].lower() == m_title:
      		  	if pd.isna(df.iloc[i][3]):
           			 return HttpResponse("<h1 style='color:red'>Sorry No Movie Link Found !!</h1> <br> <br> <a href='search'>back</a>")
       		 	else:
           			 return HttpResponse(f"<!DOCTYPE html><html><body style='background-color:lightgreen'><a href='{df.iloc[i][3]}'><h3>{df.iloc[i][18]}</h3></a><br><br><br><br><br><h1>ENJOY YOUR MOVIE</h1></body></html>")	