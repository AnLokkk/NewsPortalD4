from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import NwForm, ArForm


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'NEWS.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new1.html'
    context_object_name = 'new1'


class NwCreate(CreateView):
    form_class = NwForm
    model = Post
    template_name = 'nw_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class ArCreate(CreateView):
    form_class = ArForm
    model = Post
    template_name = 'ar_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class NwUpdate(UpdateView):
    form_class = NwForm
    model = Post
    template_name = 'nw_edit.html'
    success_url = reverse_lazy('post_list')


class ArUpdate(UpdateView):
    form_class = ArForm
    model = Post
    template_name = 'ar_edit.html'
    success_url = reverse_lazy('post_list')


class NwDelete(DeleteView):
    model = Post
    template_name = 'nw_delete.html'
    success_url = reverse_lazy('post_list')


class ArDelete(DeleteView):
    model = Post
    template_name = 'ar_delete.html'
    success_url = reverse_lazy('post_list')
