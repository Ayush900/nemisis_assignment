from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from online_portal.forms import  UpdateProfileForm
from django.views.generic.edit import UpdateView
from online_portal.models import Profile


# Create your views here.

def home(request):
    return render(request,'online_portal/home.html',{})

# def usersignup(request):
#     if request.method  == 'GET':
#         return render(request,'online_portal/signupuser.html',{'RegistrationForm':RegistrationForm(),'ProfileForm':ProfileForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(first_name = request.POST['first_name'], last_name = request.POST['last_name'] ,
#                                             username = request.POST['username'] , email = request.POST['email'],
#                                             password = request.POST['password1'] )
#             profile_form = ProfileForm(request.POST)
#             if user_form.is_valid() and profile_form.is_valid():
#                 user.save()
#                 profile_form.save()
#                 login(request , user)
#
#                 return redirect('home')
#         else:
#             return render(request,'online_portal/signupuser.html',{'RegistrationForm':RegistrationForm(),'ProfileForm':ProfileForm(),error:'The Passwords did not match'})

def usersignup(request):
    if request.method  == 'GET':
        return render(request,'online_portal/signupuser.html',{})
        # {'RegistrationForm':RegistrationForm(),'ProfileForm':ProfileForm()}
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(first_name = request.POST['first_name'], last_name = request.POST['last_name'] ,
                                                username = request.POST['username'] , email = request.POST['email'],
                                                password = request.POST['password1'] )
                # print('user:',user)
                # profile = Profile.objects.create(user=user,address = request.POST['address'] )
                # print('profile:',profile)
                user.save()
                # profile.save()
                login(request , user)
                return redirect('home')

            except IntegrityError:
                return render(request,'online_portal/signupuser.html',{'error':'The user name has already been taken!'})

        else:
            return render(request,'online_portal/signupuser.html',{'error':'The Passwords did not match'})


def loginuser(request):
    if request.method  == 'GET':
        return render(request,'online_portal/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username = request.POST['username'] , password = request.POST['password'])
        if user is None:
            return render(request,'online_portal/loginuser.html',{'form':AuthenticationForm(),'error':'The username and passwords dont match'})
        else:
            login(request , user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def userdetails(request):
    # User = get_user_model()
    users_list = User.objects.all()
    # profiles_list = Profile.objects.all()
    # profiles_list = profiles_list[:len(profiles_list)-1]
    # for i in profiles_list:
    #     print(i,' , ')
    # print(profiles_list[1].user.username)
    return render(request,'online_portal/userdetail.html' , {'users_list':users_list})

# class UserUpdateView(UpdateView):
#     # specify the model you want to use
#     model = User
#     # specify the fields
#     fields = [
#         "first_name",
#         "last_name",
#         "username",
#         "email"
#     ]
#     template_name = "online_portal/userdetail.html"
#     # can specify success url
#     # url to redirect after successfully
#     # updating details
    # success_url ="/"

@login_required
def update_profile(request , user_id):
    print('user ID :',user_id)
    # args = {}
    # instance = get_object_or_404(User, id=user_id)
    instance = User.objects.get(id=user_id)
    instance.username = request.POST['username']
    instance.first_name = request.POST['first_name']
    instance.last_name = request.POST['last_name']
    instance.email = request.POST['email']
    # instance.user.address = request.POST['address']
    instance.save()
    # us = User.objects.get(id = user_id)
    # print(type(instance))
    # form = UpdateProfile(request.POST or None, instance=instance)
    # # print(type(form))
    # if form.is_valid():
    #     form.save()
    #     return redirect('userdetails')
    return render(request, 'online_portal/userdetail.html',{})
    # if request.method != 'POST':
    #     form = UpdateProfile(instance=entry, user=request.user)
    #     return render(request,'online_portal/userdetail.html',{'form':form})
    # else:
    #     return render(request,'online_portal/userdetail.html',{'form':form})

    # if request.method == 'POST':
    #     form = UpdateProfile(request.POST,instance=request.user)
    #     # form.actual_user = request.user
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('update_profile_success'))
    # else:
    #     form = UpdateProfile()
    #     return render(request,'online_portal/update_profile.html',{'form':form})
    # args['form'] = form
    # return render(request, 'online_portal/update_profile.html', args)

@login_required
def edituserdetails(request , user_id):
    # form = UpdateProfileForm()
    if request.method  == 'GET':
        user = User.objects.get(id = user_id)
        return render(request,'online_portal/update_user.html',{'UpdateProfileForm':UpdateProfileForm(),'user':user})
        # {'RegistrationForm':RegistrationForm(),'ProfileForm':ProfileForm()}
    else:
        instance = User.objects.get(id=user_id)
        instance.username = request.POST['username']
        instance.first_name = request.POST['first_name']
        instance.last_name = request.POST['last_name']
        instance.email = request.POST['email']
        instance.save()
        return redirect('userdetails')

@login_required
def delete_user(request , user_id):
    instance = User.objects.get(id=user_id)
    instance.delete()
    return redirect('userdetails')
