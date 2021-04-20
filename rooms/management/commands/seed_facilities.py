from django.core.management.base import BaseCommand
from rooms.models                import Facility

class Command(BaseCommand):

    help = 'this command create facilities!'

    def handle(self, *args, **options):
        facilities = (
                        "Private entrance",
                        "Paid parking on premises",
                        "Paid parking off premises",
                        "Gym",
                        "Hot tub",
                        "Pool",
                    )

        for f in facilities:
            Facility.objects.create(
                name=f
            )                
        self.stdout.write(self.style.SUCCESS(f"성공적으로 퍼실리티 {len(facilities)}가 생성되었습니다."))