import random
from faker import Faker
from django.core.management.base import BaseCommand
from customer.models import Customer

class Command(BaseCommand):
    help = 'Populate Customer model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):  # Adjust the number of customers as needed
            customer = Customer(
                customerid=fake.unique.random_number(digits=5),
                companyname=fake.company(),
                contactname=fake.name(),
                contacttitle=fake.job(),
                address=fake.address(),
                city=fake.city(),
                region=fake.state(),
                postalcode=fake.zipcode(),
                country=fake.country(),
                phone=fake.phone_number(),
                fax=fake.phone_number()
            )
            customer.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated Customer model with dummy data'))
