import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as reviews_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):
    help = "This command creates many users "
    
    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=2, help="How many users do you want to create")
        
        
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                "accuracy" : lambda x: random.randint(1, 5),
                "communication" : lambda x: random.randint(1, 5),
                "cleanliness" : lambda x: random.randint(1, 5),
                "location" : lambda x: random.randint(1, 5),
                "check_in" : lambda x: random.randint(1, 5),
                "value" : lambda x: random.randint(1, 5),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users)
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rewiews created!"))