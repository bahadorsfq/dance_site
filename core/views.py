from django.shortcuts import render
from .models import GalleryImage, Album
from .models import ContactInfo
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contact.html', {'form': ContactForm(), 'success': True, 'contacts': ContactInfo.objects.all()})
    else:
        form = ContactForm()
    contacts = ContactInfo.objects.all()
    return render(request, 'core/contact.html', {'form': form, 'contacts': contacts})

def gallery(request):
    albums = Album.objects.prefetch_related('galleryimage_set').order_by('-created_at')
    return render(request, 'core/gallery.html', {'albums': albums})

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')



