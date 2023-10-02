import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from product.models import Brand , Product

def seed_brand(n):
    fake = Faker()
    images = ['2.jpeg', '3.jpeg', '4.jpeg', '5.jpg', '6.jpeg', '7.jpeg', '8.jpeg', '9.jpeg', '10.jpeg', '11.jpeg', '12.jpeg', '13.jpeg', '14.jpeg']
    for _ in range(n):
      Brand.objects.create(
      name = fake.name(),
      image = f'brands/{images[random.randint(0,12)]}'
      )
    print(f'Seed{n} Brands Successfully')

def seed_product(n):
    pass





seed_brand(5)  