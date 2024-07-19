from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Comwrite
from ..models import Sale
from ..models import Find

def index(request):
    return render(request, 'pybo/home.html', )

def guicom(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    comwrite_list = Comwrite.objects.order_by('-create_date')
    if kw:
        comwrite_list = comwrite_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(comcomment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(comcomment__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(comwrite_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'comwrite_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/comwrite_list.html', context)

def salep(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    sale_list = Sale.objects.order_by('-create_date')
    if kw:
        sale_list = sale_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)   # 질문 글쓴이 검색
        ).distinct()
    paginator = Paginator(sale_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'sale_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/sale_list.html', context)

def findp(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    find_list = Find.objects.order_by('-create_date')
    if kw:
        find_list = find_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)   # 질문 글쓴이 검색
        ).distinct()
    paginator = Paginator(find_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'find_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/find_list.html', context)

def detail(request, comwrite_id):
    comwrite = get_object_or_404(Comwrite, pk=comwrite_id)
    context = {'comwrite': comwrite}
    return render(request, 'pybo/comwrite_detail.html', context)

def saledetail(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    context = {'sale': sale}
    return render(request, 'pybo/sale_detail.html', context)

def finddetail(request, find_id):
    find = get_object_or_404(Sale, pk=find_id)
    context = {'find': find}
    return render(request, 'pybo/find_detail.html', context)

