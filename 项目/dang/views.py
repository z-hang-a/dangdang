import datetime
import json
import random
import string

from django.db import transaction
from django.shortcuts import render, HttpResponse
from carapp.car import Car as cart
from carapp.models import TAddress, Car
from indexapp.models import TBook
from adminapp.models import TUser


def car(request):
    try:
        car_items = request.session.get('car_items')
        # print(car_items, '1111')
        if car_items:
            pass
        else:
            car_items = cart()
            # request.session['car_items'] = car_items
        status = request.session.get('login')
        # print(status, '22222')
        if status:
            name = request.session.get('username')
            # print(name, '333333')
            if car_items.car_item == []:
                user_id = TUser.objects.filter(user_email=name)[0].user_id
                # print(user_id, '44444')
                book_ids = Car.objects.filter(user_id=user_id).values('book_id')
                # print(book_ids, '55555')
                for book_id in book_ids:
                    number = Car.objects.filter(user_id=user_id, book_id=book_id['book_id']).values('products_count')[0]['products_count']
                    print(book_id['book_id'], number)
                    car_items.add_item(book_id['book_id'], number)
                    request.session['car_items'] = car_items
        else:
            name = ''

        request.session['url'] = "/carapp/car/"
        return render(request, 'car.html', {
            'name': name,
            'car_items': car_items,
        })
    except:
        render(request, '404.html')

# 添加
def add_car(request):
    book_id = request.POST.get('bookid')
    number = int(request.POST.get('number', 1))
    car_items = request.session.get('car_items')
    if car_items:
        pass
    else:
        car_items = cart()
    car_items.add_item(book_id, number)
    request.session['car_items'] = car_items
    status = request.session.get('login')
    if status:
        username = request.session.get('username')
        user = TUser.objects.filter(user_email=username)[0].user_id
        dprice = TBook.objects.filter(book_id=book_id)[0].book_dprice
        price = TBook.objects.filter(book_id=book_id)[0].book_price
        result = Car.objects.create(user_id=user, book_id=book_id, products_price=dprice * number,
                                    discount_price=(price - dprice) * number, products_count=number)
        if result:
            return HttpResponse('1')
    else:
        return HttpResponse('1')


# 修改
def change(request):
    try:
        with transaction.atomic():
            book_id = request.POST.get('bookid')
            number = int(request.POST.get('number'))
            print(number,565656)
            print(book_id)
            car_items = request.session.get('car_items')
            car_items.change_item(book_id, number)
            request.session['car_items'] = car_items
            status = request.session.get('login')
            if status:
                username = request.session.get('username')
                user = TUser.objects.filter(user_email=username)[0]
                if Car.objects.filter(user_id=user.user_id, book_id=book_id):
                    item = Car.objects.filter(user_id=user.user_id, book_id=book_id)[0]
                    item.products_count = number
                    item.save()
                    print(6666666,item.products_count)
                return HttpResponse('1')
            else:
                return HttpResponse('1')
    except:
        return render(request, '404.html')


# 删除
def del_car(request):
    try:
        with transaction.atomic():
            print(3)
            book_id = request.POST.get('bookid')
            print(book_id, type(book_id), '我是删除的book——id 1111111111111111111111111')
            car_items = request.session.get('car_items')
            car_items.del_item(book_id)
            request.session['car_items'] = car_items
            status = request.session.get('login')
            if status:
                username = request.session.get('username')
                user = TUser.objects.filter(user_email=username)[0]
                item = Car.objects.filter(user_id=user.user_id, book_id=book_id)
                item.delete()
            return HttpResponse('1')
    except:
        return render(request, '404.html')


# 恢复
def recover_item(request):
    try:
        with transaction.atomic():
            print(2)
            book_id = request.POST.get('bookid')
            number = request.POST.get('number')
            car_items = request.session.get('car_items')
            car_items.recover_item(book_id)
            request.session['car_items'] = car_items
            status = request.session.get('login')
            if status:
                username = request.session.get('username')
                user = TUser.objects.filter(user_email=username)[0]
                result = Car.objects.create(user_id=user.id, book_id=book_id,
                                            products_price=car_items.car_item[-1].one_total_price,
                                            discount_price=car_items.car_item[-1].one_save_price, products_count=number)
                if result:
                    return HttpResponse('1')
            else:
                return HttpResponse('1')
    except:
        return render(request, '404.html')


# 订单


# def indent(request):
#     user=request.session.get('username')
#     user_id=TUser.objects.filter(user_email=user)
#     id=request.GET.get('id')
#     if user_id:
#         adress_ids=TAddress.objects.filter(user_id=user_id[0].user_email)
#         adress_id = TAddress.objects.filter(id=id)
#         print(adress_id,'qweqweqwe')
#         if adress_id:
#             adress=list(adress_id)
#             return JsonResponse({'adress':adress},safe=True,json_dumps_params={'default':user_default})
#         elif adress_ids:
#             user_id = TUser.objects.filter(user_email=user)[0].user_id
#             carid = DOrderiterm.objects.filter(shop_ordid=user_id)
#             s = Cart()
#             for i in carid:  # 图书id遍历
#                 lists = s.add_car(i.shop_bookid, i.shop_num)
#                 print(lists, i.shop_bookid, i.shop_num, 'iiiiiiiii')
#             carlist = s.cart_items  # 商品列表
#             total_price = s.total_price
#             save_price = s.save_price
#             return render(request, 'indent.html', {
#                                                              'adress_ids': adress_ids,
#                                                              'user': user,
#                                                             'carlist': carlist,
#                                                             'total_price': total_price,
#                                                             'save_price': save_price
#                                                         })
#             # adress_id=TAddress.objects.create(user_id=user_id[0].user_id)
#     else:
#
#         return render(request,'adminapp/login.html')

def indent(request):
    try:
        username = request.session.get('username')
        print(username)
        # print(car_items)
        car_items = request.session.get('car_items')
        user_id = TUser.objects.filter(user_email=username)[0].user_id
        # print(user_id,666666666)
        print(Car.objects.filter(user_id=6), 8888)
        cost = ''
        # for i in Car.objects.filter(user_id=user_id):
        #     print(i, 88888)
        #     print(i.book_id)
        #     if car_items:
        #         car_items.add_item(i.book_id, i.products_count)
        #         # request.session['car_items'] = car_items
        #     else:
        #         car_items = cart()
        #         car_items.add_item(i.book_id, i.products_count)
        #         request.session['car_items'] = car_items
        #     cost = car_items.total_price
        if not cost:
            cost = 0
        if not car_items:
            car_items = cart()
        address_items = TAddress.objects.filter(user_id=user_id)
        return render(request, 'indexapp/indent.html', {
            'status': username,
            'cart_items': car_items.car_item,
            'cart': car_items,
            # 'total_price': cost,
            'address_items': address_items,
        })
    except:
        return render(request,'404.html')


def indent_logic(request):
        username = request.session.get('username')
        user_id = TUser.objects.get(user_email=username).user_id
        print(user_id,99999)
    # try:
        print('进去')
        ship_man = request.POST.getlist('ship_man')
        print(ship_man)
        name = ship_man[0]
        detail_address = ship_man[1]
        zipcode = ship_man[2]
        addr_mobile = ship_man[3]
        telphone = ship_man[4]
        count= TAddress.objects.count()
        print(name)
        print(detail_address)
        print(zipcode)
        print(addr_mobile)
        print(count)
        if not TAddress.objects.filter(name=name, detail_address=detail_address, zipcode=zipcode,
                                       telphone=telphone, addr_mobile=addr_mobile, user_id=user_id):
            TAddress.objects.create(id=count+1, name=name, detail_address=detail_address, zipcode=zipcode,
                                    telphone=telphone, addr_mobile=addr_mobile, user_id=user_id)
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    # except:
    #     return HttpResponse('0')


def indent_ok(request):
    try:
            username = request.GET.get('username')
            total_price = request.GET.get('total_price')
            car_items = request.session.get('car_items')
            print(username,5555)
            print(total_price,'zzzzz')
            random_num = ''.join(random.sample(string.digits + string.digits, 11))
            username=request.session.get('username')
            print(random_num)
            if TUser.objects.filter(user_email=username):
                user = TUser.objects.filter(user_email=username)[0].user_id
                Car.objects.filter(user_id=user).delete()
            else:
                username=''
            return render(request, 'indexapp/indent ok.html', {
                'username': username,
                'total_price': total_price,
                'random_num': random_num,
                'car_items':car_items.car_item,
            })
    except:
        return render(request,'404.html')


def get_address(a):
    if isinstance(a, TAddress):
        return {'id': str(a.id), 'name': a.name, 'detail_address': a.detail_address, 'zipcode': a.zipcode,
                'telphone': a.telphone, 'addr_mobile': a.addr_mobile, 'user_id': a.user_id}


def old_address(request):
    address_id = request.POST.get('address_id')
    print(address_id)
    print(type(address_id))
    try:
        address = TAddress.objects.filter(id=int(address_id))
        json_str = json.dumps(list(address), default=get_address)
        return HttpResponse(json_str)
    except:
        return HttpResponse('0')


def demo(request):
    print('666233')
    print('diw3ejdfsafs')
