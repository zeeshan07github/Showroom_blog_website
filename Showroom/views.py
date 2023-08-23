from django.shortcuts import render, redirect ,  get_object_or_404
from .models import *
from .forms import contactform , AddNewProfile , AddNewBrand ,filters_models
from django.contrib.auth.decorators import login_required

def brand_list(request):
    brands = brand.objects.all()
    return render(request, "Showroom/brand_list.html", {'brands': brands})

def brand_detail(request, profile_id):
    
        brandss = brand.objects.get(id=profile_id)
        models = brandss.models.all()
        cars = car.objects.all()
        return render(request, "Showroom/brand_detail.html", {'brandss': brandss, "models": models  , "cars":cars})

def brand_delete(request, profile_id):
    # Get the model instance to be deleted
    model_instance = get_object_or_404(model, id=profile_id)

    # Delete the model
    model_instance.delete()

    # Redirect to the brand list view after the delete operation
    return redirect('Showroom:brand_list') # Import your Brand model

def delete_brand(request, brand_id):

    brand_to_delete = brand.objects.get(id=brand_id)
    brand_to_delete.delete()
    

    # Redirect to a relevant view after the delete operation
    return redirect('Showroom:brand_list') # Redirect to the brand list view, for example



def our_team(request):
    team=staff.objects.all()
    return render(request , "Showroom/our_team.html",{'team':team})

@login_required
def showroomss(request):
    Showroom=showroom.objects.all()
    return render(request ,  "Showroom/Showrooms.html", {'Showroom': Showroom})

def contactview(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text message: {form.cleaned_data['text']}")
 
    else:
        form = contactform()
    return render(request ,  "Showroom/contactus.html", {'form':form})

@login_required
def Newprofile(request):
    if request.method == 'POST':
        form = AddNewProfile(request.POST , request.FILES)
        if form.is_valid():
            
            if form.has_changed():
                form.save()
            return redirect('Showroom:brand_list')
 
    else:
        form = AddNewProfile()
    return render(request ,  "Showroom/newprofile.html", {'form':form})

@login_required
def Newmodel(request):
    if request.method == 'POST':
        form = AddNewBrand(request.POST , request.FILES)
        if form.is_valid():
            
            if form.has_changed():
                form.save()
                return redirect('Showroom:brand_list')
 
    else:
        form = AddNewBrand()
    return render(request ,  "Showroom/newbrand.html", {'form':form})


def filters(request):
    models = model.objects.all()
    filtered_models = models

    if request.method == 'GET':
        form = filters_models(request.GET)
        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            year = form.cleaned_data.get('year')

            if brand:
                filtered_models = filtered_models.filter(Brand=brand)
            if min_price is not None:
                filtered_models = filtered_models.filter(Car_price__gte=min_price)
            if max_price is not None:
                filtered_models = filtered_models.filter(Car_price__lte=max_price)
            if min_price is not None and max_price is not None:
                filtered_models = filtered_models.filter(Car_price__range=(min_price, max_price))
            if year:
                filtered_models = filtered_models.filter(Year_model__year=year)

    else:
        form = filters_models()

    context = {
        'form': form,
        'filtered_models': filtered_models,
    }
    return render(request, 'Showroom/filter.html', context)


