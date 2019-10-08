from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from indexapp.models import TBook, DCategory


def index_show(request):
    try:
        status=request.session.get('login')
        if status:
            user=request.session.get('username')
        else:
            user=''
        px=TBook.objects.all().order_by('-shelves_date')
        print(px[:8])
        xl=TBook.objects.all().order_by('-sales','-shelves_date')
        people=TBook.objects.all().order_by('book_dprice')
        tk=DCategory.objects.all()
        print(tk)
        return render(request, 'indexapp/index.html', {'show': px[:8], 'sele': xl[:5], 'people': people[:12], 'rx': xl[:10], 'tk':tk,'user':user})
    except:
        return HttpResponse('操作有误请重新进入！')
    #
# def Book_details(request):

def book_list(request):
    try:
        status = request.session.get('login')
        if status:
            user = request.session.get('username')
        else:
            user = ''
        id=request.GET.get('id')
        book_tyep = DCategory.objects.all()
        child = 0
        paren = 0
        if id:
            child_id = id
            paren_id = id
        else:
            child_id = 0
            paren_id = 0
        if id:
            if DCategory.objects.get(category_id=id).category_pid:
                book_sum = TBook.objects.filter(book_category=id)
                child=DCategory.objects.get(category_id=id).category_name
                paren_id=DCategory.objects.get(category_id=id).category_pid
                paren=DCategory.objects.get(category_id=paren_id).category_name

            else:
                paren= DCategory.objects.get(category_id=id).category_name
                l = []
                bookt = DCategory.objects.filter(category_pid=id)
                for i in bookt:
                    l.append(i.category_id)
                book_sum = TBook.objects.filter(book_category__in=tuple(l))
                print(id)
                print(bookt)
                print(book_sum)
        else:
            book_sum = TBook.objects.filter()

        num=request.GET.get('num')
        pagntor = Paginator(book_sum, per_page=3)
        if num:
            page = pagntor.page(num)
        else:
            page = pagntor.page(1)
        a=str(page.number-1)+':'+str(page.number+5)
        print(a)
        return render(request, 'indexapp/booklist.html', {'book_type':book_tyep, 'book_sum':page, 'box':a, 'child':child, 'paren':paren,
            'parent_id':paren_id,
            'child_id':child_id,
            'user':user,   })
    except:
        return render(request,'404.html')


# 书籍详情
def  bookdetails(request):
    try:
        book_name = request.GET.get('name')
        status = request.session.get('username')
        if not status:
            status = 0
        book = TBook.objects.filter(book_name=book_name)[0]
        if book:
            return render(request, 'indexapp/Book details.html', {
                'book': book,
                'status': status})
        return redirect('bookapp:index')
    except:
        return render(request,'404.html')

