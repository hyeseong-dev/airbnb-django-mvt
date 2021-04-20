import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils  import flatten # 2차원 배열 안의 값을 가져올 때 사용 가능
from django_seed                 import Seed
from rooms                       import models as room_models
from users                       import models as user_models


class Command(BaseCommand):

    help = 'this command create rooms!'

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many rooms do you want to create?")

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()

        all_users  = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(room_models.Room, number,{
            'name'      : lambda x: seeder.faker.address(),
            'host'      : lambda x: random.choice(all_users),    
            'room_type' : lambda x: random.choice(room_types),
            "guests"    : lambda x: random.randint(1,20),
            "beds"      : lambda x: random.randint(1,5),
            "baths"     : lambda x: random.randint(1,5),
            "bedrooms"  : lambda x: random.randint(1,5),
            "price"     : lambda x: random.randint(20000, 100000),

            })
        created_photos = seeder.execute()   # 2차원 리스트 배열로 [[?]] 이렇게 나옴.
        print(list(created_photos), '뭔데?')
        created_clean  = flatten(list(created_photos.values()))
        amenities      = room_models.Amenity.objects.all()
        facilities     = room_models.Facility.objects.all()
        rules          = room_models.HouseRule.objects.all()


        for pk in created_clean:
            # 기존 DB에 저장된 방 인스턴스를 pk로 조회해서 가져옴.
            room = room_models.Room.objects.get(pk=pk)

            # 하나의 방에 여러 사진을 만들어 주기 위해서 
            for i in range(3,random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )

            # 방 : 어메니티 = 일대다 관계 설정
            for a in amenities:
                magic_number = random.randint(0,15)
                if magic_number %2 ==0:
                    room.amenities.add(a) # db에 자동으로 저장되는 add() 메서드
            
            # 프런트에 json으로 값을 전달하기 위한 고심의 흔적
            # print([ {idx: value[0]} for idx, value in enumerate(room.amenities.values_list('name'),1)]) 
            
            # 방 : 퍼실리티 = 일대다 관계 설정
            for f in facilities:
                magic_number = random.randint(0,15)
                if magic_number %2 ==0:
                    room.facilities.add(f)

            # 방 : 룰 = 일대다 관계 설정
            for r in rules:
                magic_number = random.randint(0,15)
                if magic_number %2 ==0:
                    room.house_rules.add(r)
            
        self.stdout.write(self.style.SUCCESS(f"성공적으로 {number}개의 방이 생성되었습니다."))