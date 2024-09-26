from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from .models import Post
from .serializers import PostSerializers

class PostListView(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializers
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializers
    
#--------------------------
#بر اساس mixins
#class PostListView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericsAPIView):
#    queryset= Post.objects.all()
#    serializer_class = PostSerializers
    
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
    
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
    
#class PostDetailView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericsAPIView):
#    queryset= Post.objects.all()
#    serializer_class = PostSerializers
    
#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)
    
#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)
    
#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)

#-----------------------------------------------------
#بر اساس apiview
#class PostListView(APIView):
    #def get(self, request):
        #posts = Post.objects.all()
        #serializer = PostSerializers (posts, many =True)
        #return Response(serializer.data)
    
    #def post(self,request):
        #serializer = PostSerializers(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
#class PostDetailView(APIView):
    #def get_object(self,pk):
        #try: #--> چون داریم pk میگیریم 
            #post = Post.objects.get(pk=pk)
        #except Post.DoesNotExist:
            #raise Http404
        #return post
    
    #def get(self, request, pk):
        #post = self.get_object(pk)
        #serializer = PostSerializers(post)
        #return Response(serializer.data)
    
    #def put(self, request, pk): # آپدیت
        #post = self.get_object(pk)
        #serializer = PostSerializers(post, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #def delete(self, request, pk):
        #post = self.get_object(pk)
        #post.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)

#----------------------------------------------------
#from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Post , Comment
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework import status
#from .serializers import PostSerializers

#@api_view(['GET' ,'POST'])
#def index(request):
    #print(request.data)
    #return HttpResponse('Welcome')
    
    #pk = request.query_params.get('pk')
    #print(request.query_params)
    
    #pk = request.data.get('pk')
    #print(request.data)
    
    #try:
        #p = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
        #return Response({"detail":"post not exits"}, status= status.HTTP_404_NOT_FOUND)
    
    #serializer = PostSerializers(p)
    #print(serializer)
    #print ('-'*100)
    #print(serializer.data)
    #return Response(serializer.data)

#def post_list(request):
    #posts = Post.objects.all()
    #context ={'posts':posts}
    #return render(request, 'posts/post_list.html', context=context)

#def post_detail(request, post_id):
    #post = Post.objects.get(pk=post_id)
    #Comments = Comment.objects.filter(post=post)
    #context = {'post':post , 'comments':Comments}
    #return render(request, 'posts/post_detail.html', context=context)