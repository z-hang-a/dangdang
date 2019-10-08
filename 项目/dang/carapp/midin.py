import cart as cart
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from carapp.car import Car as cart
from carapp.models import Car
from adminapp.models import TUser, TBook


class Mymiddleware(MiddlewareMixin):
    def __init__(self,get_response):
        super().__init__(get_response)

    def process_request(self,request):
        status=request.session.get('login')
        if not status :
            if 'indent' in request.path:
                return redirect('adminapp:login')
        else:
            car_items = request.session.get('car_items')
            if not car_items:
                car_items=cart()
            username=request.session.get('username')
            user_id = TUser.objects.filter(user_email=username)[0]
            print(user_id,888888888)
            for i in car_items.car_item:
                if Car.objects.filter(book_id=i.book.book_id,user_id=user_id.user_id):
                    cart_book = Car.objects.filter(user_id=user_id.user_id,book_id=i.book.book_id)[0]
                    print(cart_book)
                    number=cart_book.products_count
                    print(int(number),'dfsafdsafdsa')
                    cart_book.products_count = int(number)
                    cart_book.save()
                else:

                    book_id = i.book.book_id
                    print(book_id)
                    # print(user,'45645646546')
                    dprice = TBook.objects.get(book_id=book_id).book_dprice
                    print(dprice)
                    price = TBook.objects.get(book_id=book_id).book_price
                    print(price)
                    Car.objects.create(user_id=user_id.user_id, book_id=book_id, products_price=dprice * i.number,discount_price=(price - dprice) * i.number, products_count=i.number)

