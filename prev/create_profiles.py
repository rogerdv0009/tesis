from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from your_app.models import Profile  # Ensure correct import

class Command(BaseCommand):
    help = 'Creates profiles for existing users who lack them'

    def handle(self, *args, **options):
        for user in User.objects.all():
            try:
                user.profile
            except Profile.DoesNotExist:
                Profile.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f'Created profile for {user.username}'))

        self.stdout.write(self.style.SUCCESS('Profile creation complete!'))
