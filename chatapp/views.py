from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q  # Correct import for Q
from .models import ChatMessage

@login_required
def home(request):
    users = User.objects.exclude(id=request.user.id)  # Get all other users
    user_status = []

    for user in users:
        # Get the last message between the logged-in user and the other user
        last_message = ChatMessage.objects.filter(
            (Q(sender=request.user) & Q(receiver=user)) |
            (Q(sender=user) & Q(receiver=request.user))
        ).order_by('-timestamp').first()

        # Check if the last message is unread and was sent by the other user
        is_unread = last_message and last_message.receiver == request.user and not last_message.read
        user_status.append({'user': user, 'is_unread': is_unread})

    return render(request, 'home.html', {'user_status': user_status})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)  # Logs out the current user
    return redirect('/login/')  # Redirect to the login page

@login_required
def chat(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    # Mark unread messages as read
    ChatMessage.objects.filter(sender=receiver, receiver=request.user, read=False).update(read=True)

    # Get all messages between the logged-in user and the receiver
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(receiver=receiver)) |
        (Q(sender=receiver) & Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            ChatMessage.objects.create(sender=request.user, receiver=receiver, message=message_text)

    return render(request, 'chat.html', {'receiver': receiver, 'messages': messages})
