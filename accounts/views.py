from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from accounts.forms import (
        RegistrationForm, 
        EditProfileForm,
        EditUserInfoForm
)
from accounts.models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance = request.user)

        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


class EditUserInfo(TemplateView):
    template_name = 'accounts/edit_user_info.html'

    def get(self, request):
        form = EditUserInfoForm()
        posts = UserProfile.city

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        profile = request.user.userprofile
        form = EditUserInfoForm(request.POST, instance = profile)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            city = form.cleaned_data['city']
            website = form.cleaned_data['website']
            phone = form.cleaned_data['phone']
            profile_image = form.cleaned_data['profile_image']
            form =  EditUserInfoForm()
            return redirect('accounts:view_profile')

        args = {
            'form': form, 
            'city': city,
            'website': website,
            'profile_image': profile_image,
        }
        return render(request, self.template_name, args)   

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user = request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
