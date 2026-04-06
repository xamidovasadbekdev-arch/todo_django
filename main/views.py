from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TodoForm
from .models import Todo


class HomePageView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "home.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Todo.objects.filter(user=self.request.user)
        context['total'] = qs.count()
        context['pending'] = qs.filter(status='pending').count()
        context['in_progress'] = qs.filter(status='in_progress').count()
        context['completed'] = qs.filter(status='completed').count()
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo_form.html"
    form_class = TodoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo_form.html"
    form_class = TodoForm
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return redirect('home')
