from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Verifica os superusuários existentes'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        superusers = User.objects.filter(is_superuser=True)
        if superusers.exists():
            for user in superusers:
                self.stdout.write(self.style.SUCCESS(f"Superusuário: {user.username} - Email: {user.email}"))
        else:
            self.stdout.write(self.style.WARNING("Nenhum superusuário encontrado."))
