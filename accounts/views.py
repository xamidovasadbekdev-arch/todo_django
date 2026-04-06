from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import UserForm, ProfileForm, RegisterForm
from .models import UserProfile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    context_object_name = "profile"
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user.profile


# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     fields = ['avatar', 'bio']
#     template_name = 'accounts/profile_edit.html'
#     success_url = reverse_lazy('profile')
#
#     def get_object(self):
#         return self.request.user.profile
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.method == 'POST':
#             context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
#         else:
#             context['user_form'] = UserForm(instance=self.request.user)
#         return context
#
#     def form_valid(self, form):
#         user_form = UserForm(self.request.POST, instance=self.request.user)
#         if user_form.is_valid():
#             user_form.save()
#         return super().form_valid(form)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)

