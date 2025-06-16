import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    all_passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

    print('Всего пропусков', len(all_passcards))
    print('Активных пропусков', len(active_passcards))
