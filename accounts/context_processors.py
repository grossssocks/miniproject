from vendor.models import Vendor
from django.conf import settings
from accounts.models import UserProfile



def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except:
        vendor = None
    return dict(vendor=vendor)