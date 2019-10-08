from indexapp.models import TBook


class Car_item():
    def __init__(self, book, number):  # book为model对象
        self.book = book
        self.number = int(number)

    def sum(self):
        self.one_total_price = float(self.book.book_dprice) * int(self.number)
        self.one_save_price = float(self.book.book_price - self.book.book_dprice) * int(self.number)


class Car():
    def __init__(self):
        self.car_item = []
        self.del_car_item = []
        self.total_price = 0
        self.save_price = 0

    def sums(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.car_item:
            self.total_price += float(float(i.book.book_dprice) * int(i.number))
            self.save_price += float((float(i.book.book_price) - float(i.book.book_dprice)) * int(i.number))

    def add_item(self, book_id, number=1):
        for i in self.car_item:
            print(number, 127)
            print(i.book.book_id)
            print(book_id)
            if int(i.book.book_id) == int(book_id):
                i.number += int(number)
                i.sum()
                self.sums()
                # print('添加成功')
                return
        print(number,'添加成功')
        self.car_item.append(Car_item(TBook.objects.filter(book_id=book_id)[0], 1))
        self.sums()

    def del_item(self, book_id):
        print('进入删除aaaaaaaaaaaaaaaaaaaaaaaaa')
        for i in self.car_item:
            print('进入循环aaaaaaaaaaaaaaaaaaaaaaaaa')
            if int(i.book.book_id) == int(book_id):
                self.car_item.remove(i)
                self.del_car_item.append(i)
        self.sums()

    def recover_item(self, book_id):
        for i in self.del_car_item:
            if int(i.book.book_id) == int(book_id):
                self.del_car_item.remove(i)
                self.add_item(book_id)
        self.sums()

    def change_item(self, book_id, number):
        for i in self.car_item:
            if int(i.book.book_id) == int(book_id):
                i.number = int(number)
                i.sum()
        self.sums()


