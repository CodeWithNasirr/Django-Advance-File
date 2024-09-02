from faker import Faker
from test_study.models import *
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



# Bulk Create And Delete and Update
import time
def create_Cat(number):
    start_time = time.time()
    create=[Category(name=fake.name())for i in range(number)]
    # create = []
    # for _ in range(number):
    #     create.append(Category(name=fake.name()))
    Category.objects.bulk_create(create)
    end_time = time.time()
    print(f"Created {number} categories in {end_time - start_time:.2f} seconds.")

# create_Cat(100000)



def delete():
    Category.objects.all().delete()

# def update(name):
#     print(Student.objects.filter(name__icontains=name).count())
#     print(Student.objects.filter(name__icontains=name).update(name='FARHA'))
# update('Chandran')


def xyz():
    my_college=Collage.objects.all()
    students = Student.objects.filter(collage__in=my_college, gender='Male')
    print(students)

def bulk_update_is_deleted():
    # Get the primary keys of the first 50 categories
    category_ids = Category.objects.values_list('id', flat=True)[:50]
    # # Perform the bulk update using the retrieved primary keys
    updated_count = Category.objects.filter(id__in=category_ids).update(is_deleted=True)
    print(f"Updated {updated_count} categories as deleted.")
