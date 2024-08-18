from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Library, Book  # Ensure you're importing the models

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a homepage or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile  # Make sure UserProfile is imported

# Helper function to check if a user is an Admin
def is_admin(user):
    return UserProfile.objects.filter(user=user, role='Admin').exists()

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Helper function to check if a user is a Member
def is_member(user):
    return UserProfile.objects.filter(user=user, role='Member').exists()

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Helper function to check if a user is a Librarian
def is_librarian(user):
    return UserProfile.objects.filter(user=user, role='Librarian').exists()

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')