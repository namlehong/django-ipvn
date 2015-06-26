from .models import IpRange
import random


def generate_ip():
    ip_count = IpRange.objects.count()
    ip_range = IpRange.objects.all()[random.randrange(0, ip_count)]
    return ip_range.generate()