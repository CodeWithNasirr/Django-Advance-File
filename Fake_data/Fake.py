from faker import Faker
import random

fake=Faker('en_IN')

def xyzx(record=10)->None:
    for i in range(record):
        first_name=fake.text(max_nb_chars=5)
        last_name=fake.text(max_nb_chars=10)
        email=fake.email()
        date=fake.date()
        x=Customer(first_name=first_name,last_name=last_name,email=email,date_joined=date)
        x.save()

#Speed Up Method
    # start=time.time()
    # create=[Customer(first_name=fake.text(max_nb_chars=5),last_name=fake.text(max_nb_chars=10),email=fake.email(),date_joined=fake.date())for _ in range(number)]
    # Customer.objects.bulk_create(create)
    # end=time.time()
    # print(f"Created {number} of Data with in {end-start:.2f} Sec")


# def update(record=111) -> None:
#     pubs=Publisher.objects.all()
#     books=Book.objects.all()[:record]
#     for book in books:
#         pub=random.choice(pubs)
#         book.publisher = pub
#         book.save()


def xyz():
    my_college=Collage.objects.all()
    students = Student.objects.filter(collage__in=my_college, gender='Male')
    print(students)
