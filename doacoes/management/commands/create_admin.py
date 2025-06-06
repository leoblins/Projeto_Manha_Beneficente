from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Remove qualquer superusuário e cria um novo com credenciais fixas'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'leoblins'
        email = 'leoblins@gmail.com'
        password = 'Sardinha221405@'

        # Apaga todos os superusuários existentes
        superusers = User.objects.filter(is_superuser=True)
        for user in superusers:
            self.stdout.write(self.style.WARNING(f'Removendo superusuário: {user.username}'))
            user.delete()

        # Cria novo superusuário
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuário {username} criado com sucesso'))
        else:
            self.stdout.write(self.style.WARNING(f'Usuário {username} já existe, mas não é superusuário'))
