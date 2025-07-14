from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or "تصویر بدون عنوان"


class ContactInfo(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'اینستاگرام'),
        ('telegram', 'تلگرام'),
        ('whatsapp', 'واتساپ'),
        ('youtube', 'یوتیوب'),
        ('other', 'سایر'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    label = models.CharField(max_length=100)  # مثل: "پیج آموزش رقص"
    link = models.URLField()  # آدرس لینک (مثلاً https://instagram.com/...)

    def __str__(self):
        return f"{self.get_platform_display()} - {self.label}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
