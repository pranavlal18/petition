from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Petition, Signature
from .forms import PetitionForm

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'complaints/petition_list.html', {'petitions': petitions})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Petition
from .forms import PetitionForm

@login_required


def create_petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user  # Set the current user as the creator
            petition.save()
            return redirect('petition_list')  # Redirect to the petition list or success page
    else:
        form = PetitionForm()
    
    return render(request, 'complaints/create_petition.html', {'form': form})




from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Petition, Signature

@login_required
def sign_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)

    # Check if the user has already signed this petition
    if request.user in petition.signatures.all():
        messages.warning(request, "You have already signed this petition.")
        return redirect('petition_detail', petition_id=petition.id)

    # Create a new signature
    petition.signatures.add(request.user)
    messages.success(request, "You have successfully signed the petition!")
    return redirect('petition_detail', petition_id=petition.id)



def contract(request):
        return render(request, 'complaints/contract.html')

def about(request):
        return render(request, 'complaints/about.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# User Registration View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'complaints/signup.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Profile View
@login_required
def profile(request):
    return render(request, 'complaints/profile.html')

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Petition
from .forms import PetitionForm  # Assuming you have a form for your Petition model

@login_required
def edit_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)

    # Check if the user is the creator of the petition
    if petition.created_by != request.user:
        messages.error(request, "You are not allowed to edit this petition.")
        return redirect('petition_list')  # Redirect to the petition list or any other appropriate page

    if request.method == 'POST':
        form = PetitionForm(request.POST, instance=petition)
        if form.is_valid():
            form.save()
            messages.success(request, "Petition updated successfully!")
            return redirect('petition_detail', petition_id=petition.id)
    else:
        form = PetitionForm(instance=petition)

    return render(request, 'complaints/edit_petition.html', {'form': form, 'petition': petition})


from django.shortcuts import render, get_object_or_404
from .models import Petition

def petition_detail(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    return render(request, 'complaints/petition_detail.html', {'petition': petition})


from django.shortcuts import render
from .models import Petition

# views.py
from django.shortcuts import render
from .models import Petition

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'complaints/petition_list.html', {'petitions': petitions})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Petition

@login_required
def my_petitions(request):
    petitions = Petition.objects.filter(created_by=request.user)
    return render(request, 'complaints/my_petitions.html', {'petitions': petitions})
