from django.core.management.base import BaseCommand
from ipvn.models import IpRange

class Command(BaseCommand):
    args = '<mode> <option>'
    help = 'Create Scan Request'

    def handle(self, *args, **options):
        with open(args[0]) as infile:
            content = infile.readlines()
            content = [item.split(',') for item in content]
            for item in content:
                if len(item) >= 2:
                    try:
                        IpRange.objects.get_or_create(
                            from_ip=item[0],
                            to_ip=item[1]
                        )
                    except Exception as e:
                        print e


