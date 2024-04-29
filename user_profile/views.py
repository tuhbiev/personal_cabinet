from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from user_profile.forms import UserEditForm
from user_profile.models import User


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

