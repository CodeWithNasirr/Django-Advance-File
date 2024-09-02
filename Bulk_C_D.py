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