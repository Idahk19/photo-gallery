from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Photo, PhotoReaction, Profile
from django.contrib.auth.decorators import login_required


def home(request):
    tag = request.GET.get('tag', '').strip()

    if tag:
        photos = Photo.objects.filter(
            tags__icontains=tag
        ).order_by('-uploaded_at')
    else:
        photos = Photo.objects.all().order_by('-uploaded_at')

    for photo in photos:
        photo.like_count = PhotoReaction.objects.filter(
            photo=photo,
            reaction='like'
        ).count()

        photo.dislike_count = PhotoReaction.objects.filter(
            photo=photo,
            reaction='dislike'
        ).count()

    return render(request, 'home.html', {
        'photos': photos,
        'selected_tag': tag
    })


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'register.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already exists.'
            })

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        Profile.objects.create(user=user)

        # Show success message
        return render(request, 'register.html', {
            'success': True
        })

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return render(request, 'login.html', {
                'success': True
            })

        return render(request, 'login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def photo_detail(request, id):
    photo = get_object_or_404(Photo, id=id)

    return render(request, 'photodetail.html', {
        'photo': photo
    })

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'profile.html', {
        'profile': profile
    })

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.username = request.POST.get('username')
        profile.bio = request.POST.get('bio')

        request.user.save()
        profile.save()

        return redirect('profile')

    return render(request, 'edit_profile.html', {
        'profile': profile
    })

@login_required
def react_to_photo(request, id):
    photo = get_object_or_404(Photo, id=id)

    if request.method == 'POST':
        reaction = request.POST.get('reaction')

        if reaction not in ['like', 'dislike']:
            return redirect('home')

        existing_reaction = PhotoReaction.objects.filter(
            user=request.user,
            photo=photo
        ).first()

        if existing_reaction:
            if existing_reaction.reaction == reaction:
                # Remove reaction if user clicks the same button again
                existing_reaction.delete()
            else:
                # Change reaction
                existing_reaction.reaction = reaction
                existing_reaction.save()
        else:
            # Create new reaction
            PhotoReaction.objects.create(
                user=request.user,
                photo=photo,
                reaction=reaction
            )

    return redirect('home')