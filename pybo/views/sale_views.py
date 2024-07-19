from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import SaleForm
from ..forms import Sale

@login_required(login_url='common:login')
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            sale = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            sale.author = request.user  # author 속성에 로그인 계정 저장
            sale.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            sale.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:salep')
    else:
        form = SaleForm()
    context = {'form': form}
    return render(request, 'pybo/sale_form.html', context)

@login_required(login_url='common:login')
def sale_delete(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    if request.user != sale.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:saledetail', sale_id=sale.id)
    sale.delete()
    return redirect('pybo:salep')