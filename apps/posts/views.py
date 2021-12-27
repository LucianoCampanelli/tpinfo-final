from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Comentario
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListarPosts(LoginRequiredMixin, ListView):
	model = Post
	template_name = "posts/postsList.html"
	context_object_name = "posts"
	#def get_queryset(self):
	#	noticias = Noticia.objects.all().order_by('-fecha_creacion')
	#	return noticias

class DetallePost(LoginRequiredMixin, DetailView):
	model = Post
	template_name="posts/post_detail.html"
	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['comentarios'] = Comentario.objects.all()
		return data 

def index(request):
    return render(
		request,
        'index.html',
	)

class CrearPost(CreateView):
	model = Post
	success_url='/posts'
	form_class = PostForm
	template_name = 'posts/post_form.html'

class UpdatePost(UpdateView):
	model = Post
	success_url='/posts'
	form_class = PostForm
	template_name = 'posts/post_update_form.html'