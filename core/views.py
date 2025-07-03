from django.shortcuts import render
from .models import GalleryImage
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
    images = GalleryImage.objects.order_by('-uploaded_at')
    return render(request, 'core/gallery.html', {'images': images})

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')



