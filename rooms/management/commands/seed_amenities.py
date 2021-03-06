from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "this command create amenities!"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--times',
    #         help='How many times do you want me to tell you that I love you?')

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"성공적으로 어메니티 {len(amenities)}가 생성되었습니다!"))
