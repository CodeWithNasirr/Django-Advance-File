
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Study.settings'
django.setup()
from django.db.models import Count, Sum, Avg, Max, Min, F, Value, CharField, IntegerField, Q, Case, When, ExpressionWrapper, DurationField, OuterRef, Subquery, Prefetch,Exists
from django.db.models.functions import Concat, Coalesce, Length, Upper, Lower, TruncMonth
from test_study.models import *


# 1. Count the number of books each author has written.
def handle():
    authors=Author.objects.annotate(Books=Count('books'))
    for author in authors:
        books=Book.objects.filter(author=author)
        print(f"Author Name: {author.author_name} totalBooks: {author.Books}")
        for book in books:
            print(f'Book Name: {book.book_name}')

# 2. Calculate the toatl price  for each Author book.
def handle1():
    authors=Author.objects.annotate(Total_price=Sum('books__price'))

    for author in authors:
        print(f"Author Name: {author.author_name} Total_price: {author.Total_price}")


# 3. Find the average price of books per Author.

def handle2():
    authors=Author.objects.annotate(Avg_price=Avg('books__price'))
    for author in authors:
        print(f"Author Name: {author.author_name} Avg_price: {author.Avg_price}")



# 5. Annotate authors with the number of published books.

def handle3():
    authors=Author.objects.annotate(book_published=Count('books__published_date')).filter(book_published__gte=1)
    for author in authors:
        print(f"Author Name: {author.author_name} book_published: {author.book_published}")



# 9. Annotate Customber with their author's full name.
def handle4():
    Customers=Customer.objects.annotate(Customer_name=Concat(F('first_name'), Value(' '), F('last_name')))
    for custumer in Customers:
        print(f"Custumber NAme: {custumer.Customer_name}")


# 10. Count the number of books by each publisher.
def handle5():
    pubs=Publisher.objects.annotate(book_count=Count('books')).filter(book_count__gte=1)
    for pub in pubs:
        print(f'Publsiher Name: {pub.name} book_count: {pub.book_count}')
        books=Book.objects.filter(publisher=pub)
        for index,book in enumerate(books,start=1):
            print(f"Book-{index} : {book.book_name}")

#SubQueryMEthod
#Latest Book For Each Author 
    latest_book = Book.objects.filter(
        author=OuterRef('pk')
    ).order_by('-published_date').values('book_name')[:1]
    
    authors = Author.objects.annotate(
        latest_book_name=Subquery(latest_book, output_field=CharField())
    )
    author_with_books=authors.filter(latest_book_name__isnull=False)

    for author in author_with_books:
        print(f"Author Name: {author.author_name}, Latest Book: {author.latest_book_name}")

    # authors = Author.objects.all(
    #     # latest_book_name=Subquery(latest_book, output_field=CharField())
    # )
    # for author in authors:
    #     books = Book.objects.filter(
    #     author=author).order_by('-published_date').first()
    #     if books:
    #         print(f"Author Name: {author.author_name}, Latest Book: {books.book_name}")

# SubQueryMEthod
# Total Price Of Book Published in 2023 for Each Authors 
def handle7():
    books = Book.objects.filter(
        author=OuterRef('pk'),
        published_date__year=2023
    ).annotate(total_price=Sum('price')).values('total_price')
    
    authors = Author.objects.annotate(total_price=Subquery(books),book_count=Count("books",filter=Q(books__published_date__year=2023 ))).filter(book_count__gte=1)
    
    for author in authors:
        books=Book.objects.filter(author=author,published_date__year=2023)
        for book in books:
            print(f"Author Name: {author.author_name} BookName: {book.book_name} Total Price: {author.total_price}")


# SubQueryMEthod
# Count Of Books Published By Each Author
def handle8():
    books=Book.objects.filter(author=OuterRef('pk')).values('author').annotate(total_books=Count('id')).values('total_books')
    authors=Author.objects.annotate(total_books=Subquery(books)).filter(total_books__gte=1)
    for author in authors:
        print(f"The Author Name: {author.author_name} Total_Books: {author.total_books} ")
        books=Book.objects.filter(author=author)
        for index,book in enumerate (books,start=1):
            print(f" Books{index}: {book.book_name} Pub_date: {book.published_date}")


    # authors=Author.objects.annotate(book_count=Count('books')).filter(book_count__gte=1)
    # for author in authors:
    #         print(f"The Author Name: {author.author_name} Total_Books: {author.book_count} ")
    #         books=Book.objects.filter(author=author)
    #         for index,book in enumerate (books,start=1):
    #             print(f" Books{index}: {book.book_name} Pub_date: {book.published_date}")


# Calculate Total Earing and Total Book in 2023
def handles9():
    authors = Author.objects.annotate(
        total_earing=Sum('books__price'),
        book_count=Count("books",filter=Q(books__published_date__year__gte=2023))).filter(book_count__gte=1)
    for author in authors:
        books=Book.objects.filter(author=author)
        print(f"Author Name {author.author_name} BookPrice: {author.total_earing} book_count {author.book_count}")

        for book in books:
            print(f"Bookname: {book.book_name} ")



#1. Count the number of reviews per book and order by the number of reviews:
def handle1():
    books_with_review=Book.objects.annotate(review=Count('reviews')).order_by('-review').filter(review__gte=1)
    for book in books_with_review:
        print(f"Book: {book.book_name}, Reviews: {book.review}")

#2. Calculate the average rating of each book:
def handle2():
    books_with_Rating=Book.objects.annotate(avg=Avg('reviews__rating')).order_by('-avg').filter(avg__gte=1)
    for book in books_with_Rating:
        print(f"Book: {book.book_name}, Avg_Rating: {book.avg}")



#Get total number of students in each collage:
def handle3():
    collages=Collage.objects.annotate(student_count=Count('student'))
    for collage in collages:
        print(f"Collage Name: {collage.collage_name} Total_Studnt: {collage.student_count}")

#3 Calculate the total price of orders for each customer:
def handle4():
    # Annotate customers with the total price of their orders, filtering those with total_price >= 1
    customers = Customer.objects.annotate(total_price=Sum('orders__total_price')).order_by('-total_price').filter(total_price__gte=1)
    
    for customer in customers:
        # Print customer details
        print(f'Customer Name: {customer.first_name} {customer.last_name}, Total Price: {customer.total_price}')
        
        # Access the orders of this customer

        for order in customer.orders.all():
            # Access each order's related order items and their associated products
            for order_item in order.orderitems.all():
                product=order_item.product  # Add the product's name to the set
        
        # Print the products ordered by the customer
        print(f"Products: {product.name}")

#4 Calculate a Customer total Order And His oreder details ?
def handle5():
    customers=Customer.objects.annotate(total_order=Count('orders')).order_by('-total_order').filter(total_order__gte=1)
    for customer in customers:
        print(f'CustumerName: {customer.first_name} {customer.last_name} total_order: {customer.total_order}')
        orders=Order.objects.filter(customer=customer)
        index=1
        for order in orders:
            order_item=OrderItem.objects.filter(order=order)
            for item in  (order_item):
                print(f" {index}: {item.product.name} Price: {item.product.price} Quntity: {item.quantity}")
                index+=1

#Annotate products with the count of orders they have been in. and all access his details
def handle6():
    products=Product.objects.annotate(Count_order=Count('orderitems')
                                      )
    for pdt in products:
        print(f"Name: {pdt.name} Total_Order: {pdt.Count_order}")
        for index,order_item in enumerate (pdt.orderitems.all(),start=1):  #Access related OrderItems
            order=order_item.order
            print(f" {index}:Discount: {order_item.discount} Price:{pdt.price} Qty: {order_item.quantity}")



# SubQueryMEthod
# Avg Price Of Books Published By Each Author
def handle10():
    books=Book.objects.filter(author=OuterRef('pk')).values('author').annotate(Avg_Price=Avg('price')).values('Avg_Price')
    authors=Author.objects.annotate(Avg_Price=Subquery(books)).filter(Avg_Price__isnull=False)
    for author in authors:
        print(f"Author Name: {author.author_name} AvgPrice: {author.Avg_Price}")


# SubQueryMEthod
# Most Expensive Book For Each Author
def handle11():
    books=Book.objects.filter(author=OuterRef('id')).values('author').order_by('-price')
    authors=Author.objects.annotate(Expensive=Subquery(books.values('price')),
                                   Expensive_Book_name=Subquery(books.values('book_name'))).filter(Expensive__gte=1)
    for author in authors:
        print(f"Author Name: {author.author_name} ExpensiveBook: {author.Expensive} BookName: {author.Expensive_Book_name} ")

# SubQueryMEthod
# Author With Atleast One Book Priced over 50rs
def handle12():
    books=Book.objects.filter(author=OuterRef('id'),
                              price__gte=50,
                              price__lte=60).order_by('-price').values('price')
    authors=Author.objects.annotate(Price_50=Subquery(books),
                                    Book_name=Subquery(books.values('book_name'))).filter(Price_50__isnull=False)
    for author in authors:
        print(f"Author Name: {author.author_name} Price: {author.Price_50} Name_Book: {author.Book_name}")

# SubQueryMEthod
# Total Earning OF Each Author

def handle13():
    books = Book.objects.filter(author=OuterRef('id')).values('author').annotate(total_earning=Sum('price'))
    authors=Author.objects.annotate(total=Subquery(books.values('total_earning'))).filter(total__gte=1)
    for author in authors:
        print(f"Author Name: {author.author_name} total_earning: {author.total}")

# SubQueryMEthod
# Author With Books Published in Each Month of 2023

def handle14():
    books=Book.objects.filter(author=OuterRef('id'),
                              published_date__year=1999,
                              published_date__month=1).values('author')
    authors=Author.objects.annotate(
        has_books_in_jan=Exists(books),
        Jan_Book=Subquery(books.values('book_name')[:1]),
        pub=Subquery(books.values('published_date')[:1])
        ).filter(has_books_in_jan=True)

    for author in authors:
        print(f"Author Name: {author.author_name}")
        print(f"Januwary: {author.Jan_Book} Date: {author.pub}")
