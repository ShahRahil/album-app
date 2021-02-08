from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.

def gallery(request):
    query = request.GET.get('query')
    if query == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=query)
    categories = Category.objects.all()
    
    content = {'categories': categories, 'photos': photos}
    return render(request,'images/gallery.html', content)

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'images/add.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    content = {'photo': photo}
    return render(request,'images/photo.html', content)