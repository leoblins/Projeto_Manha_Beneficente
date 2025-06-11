from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria superusuários fixos se ainda não existirem'

    def handle(self, *args, **options):
        User = get_user_model()

        superusers = [
            {"username": "leoblins", "email": "leoblins@gmail.com", "password": "Sardinha221405@"},
            {"username": "Web3admin", "email": "web3admin@email.com", "password": "Senha123"},
        ]

        for user_data in superusers:
            usuario = User.objects.filter(username=user_data["username"]).first()

            if usuario and usuario.is_superuser:
                self.stdout.write(f"Superusuário '{user_data['username']}' já existe.")
            elif usuario:
                self.stdout.write(self.style.WARNING(f"Usuário '{user_data['username']}' existe, mas não é superusuário."))
            else:
                User.objects.create_superuser(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=user_data["password"]
                )
                self.stdout.write(self.style.SUCCESS(f"Superusuário '{user_data['username']}' criado com sucesso."))
