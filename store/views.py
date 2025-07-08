from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Package
from .models import UserPackage
from .models import Purchase
from .models import OrientalMusic
from .forms import RegisterForm
from django.contrib.auth import login
import requests
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from store.models import Package, UserPackage

@login_required
def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)

    # آیا کاربر اجازه مشاهده ویدئو را دارد؟
    can_view = UserPackage.objects.filter(user=request.user, package=package, activated=True).exists()

    return render(request, 'store/package_detail.html', {
        'package': package,
        'can_view_video': can_view,
    })


def start_payment(request, pk):
    return HttpResponse("💳 پرداخت آنلاین موقتاً غیرفعال است. لطفاً بعداً مراجعه کنید.")

def verify_payment(request):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if status != 'OK':
        return HttpResponse("پرداخت توسط کاربر لغو شد")

    package_id = request.session.get('payment_package_id')
    if not package_id:
        return HttpResponse("خطا: اطلاعات پکیج پیدا نشد")

    package = get_object_or_404(Package, pk=package_id)
    amount = int(package.price * 10)

    data = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": amount,
        "authority": authority,
    }

    response = requests.post(
        'https://api.zarinpal.com/pg/v4/payment/verify.json',
        json=data
    ).json()

    if response.get('data') and response['data']['code'] == 100:
        # جلوگیری از تکراری بودن سفارش
        if not Purchase.objects.filter(user=request.user, package=package).exists():
            Purchase.objects.create(
                user=request.user,
                package=package
            )

        del request.session['payment_package_id']  # پاک کردن اطلاعات بعد از پرداخت

        return HttpResponse(f"✅ پرداخت با موفقیت انجام شد. کد رهگیری: {response['data']['ref_id']}")
    else:
        return HttpResponse("❌ پرداخت ناموفق: " + str(response.get('errors')))



def oriental_music_list(request):
    musics = OrientalMusic.objects.order_by('-upload_date')
    return render(request, 'store/oriental_music_list.html', {'musics': musics})

def package_list(request):
    packages = Package.objects.all()  
    return render(request, 'store/package_list.html', {'packages': packages})

@login_required
def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    # چک کن که آیا کاربر برای این پکیج فعال است؟
    try:
        user_package = UserPackage.objects.get(user=request.user, package=package, activated=True)
    except UserPackage.DoesNotExist:
        return HttpResponse("شما اجازه دسترسی به این ویدئو را ندارید. لطفاً ابتدا عضو شوید یا فعال سازی دریافت کنید.")

    return render(request, 'store/package_detail.html', {'package': package})

@login_required
def purchase_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    Purchase.objects.create(user=request.user, package=package)
    return render(request, 'store/purchase_success.html', {'package': package})

@login_required
def my_purchases(request):
    purchases = Purchase.objects.filter(user=request.user).select_related('package').order_by('-purchase_date')
    return render(request, 'store/my_purchases.html', {'purchases': purchases})

def start_purchase(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'store/start_purchase.html', {'package': package})

def register_view(request):
    next_url = request.GET.get('next', '/')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار بعد از ثبت‌نام
            return redirect(next_url)
    else:
        form = RegisterForm()
    
    return render(request, 'store/register.html', {'form': form, 'next': next_url})