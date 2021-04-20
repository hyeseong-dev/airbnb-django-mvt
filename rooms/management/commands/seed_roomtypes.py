from django.core.management.base import BaseCommand
from rooms.models                import RoomType

NAME = 'Room Type'

class Command(BaseCommand):

    help = f'this command create {NAME}!'

    def handle(self, *args, **options):
        roomtypes = (
                    'Hotel Room',
                    'Shared Room',
                    'Private Room',
                    'Entire Room',
                    )

        for f in roomtypes:
            RoomType.objects.create(
                name=f
            )                
        self.stdout.write(self.style.SUCCESS(f"성공적으로 {NAME} {len(roomtypes)}개가 생성되었습니다."))