import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

from django.contrib.admin.utils import flatten  # 2차원 배열 안의 값을 가져올 때 사용 가능
from django_seed import Seed

from reservations import models as reservation_models
from rooms import models as room_models
from users import models as user_models

NAME = "reservations"


class Command(BaseCommand):

    help = f"this command create {NAME}!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        created_rooms = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"성공적으로 {number}개의 {NAME}이 생성되었습니다."))