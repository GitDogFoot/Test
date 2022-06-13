from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


class PostList(ListView):
  model = Post


class PostDetail(DetailView):
  model = Post


class PostCreate(CreateView):
  model = Post
  form_class = PostForm

