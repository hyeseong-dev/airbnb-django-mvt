import random
from django.core.management.base import BaseCommand

from django.contrib.admin.utils import flatten  # 2차원 배열 안의 값을 가져올 때 사용 가능
from django_seed import Seed

from rooms import models as room_models
from users import models as user_models
from reviews import models as reviews_models


class Command(BaseCommand):

    help = "this command create reviews!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "cleanliness": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"성공적으로 {number}개의 리뷰가 생성되었습니다."))