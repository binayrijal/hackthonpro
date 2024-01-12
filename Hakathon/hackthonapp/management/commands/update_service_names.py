# yourapp/management/commands/update_service_names.py

from django.core.management.base import BaseCommand
from hackthonapp.models import service_name

class Command(BaseCommand):
    help = 'Update service names with the latest information'

    def handle(self, *args, **options):
        try:
            service_name.update_with_latest_updates()
            self.stdout.write(self.style.SUCCESS('Service names updated successfully.'))
        except Exception as e:
            # Log the error, notify administrators, or handle it appropriately
            self.stderr.write(self.style.ERROR(f'Error updating service names: {e}'))
