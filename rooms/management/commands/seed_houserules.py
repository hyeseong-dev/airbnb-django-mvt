from django.core.management.base import BaseCommand
from rooms.models                import HouseRule

NAME = 'House Rules'

class Command(BaseCommand):

    help = f'this command create {NAME}!'

    def handle(self, *args, **options):
        house_rules = (
                        'DO NOT SMOKE',
                        'PETS NOT ALLOWED',
                        'PARTY NOT ALLOWED',
                    )

        for h in house_rules:
            HouseRule.objects.create(
                name=h
            )                
        self.stdout.write(self.style.SUCCESS(f"성공적으로 {NAME} {len(house_rules)}개가 생성되었습니다."))