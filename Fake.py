from faker import Faker
from test_study.models import *
import random

fake=Faker('en_IN')

def xyzx(record=10)->None:
    # authors = Author.objects.all()
    # for i in range(record):
    #     author=random.choice(authors)
    #     price=random.randint(10,100)
    #     book_name = fake.text(max_nb_chars=20)
    #     published_date=fake.date()
    #     x = Book(author=author,price=price,book_name=book_name,published_date=published_date)
    #     x.save()
    for i in range(record):
        first_name=fake.text(max_nb_chars=5)
        last_name=fake.text(max_nb_chars=10)
        email=fake.email()
        date=fake.date()
        x=Customer(first_name=first_name,last_name=last_name,email=email,date_joined=date)
        x.save()
# def update(record=111) -> None:
#     pubs=Publisher.objects.all()
#     books=Book.objects.all()[:record]
#     for book in books:
#         pub=random.choice(pubs)
#         book.publisher = pub
#         book.save()
