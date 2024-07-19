from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import FindForm
from ..forms import Find

@login_required(login_url='common:login')
def find_create(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            find = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            find.author = request.user  # author 속성에 로그인 계정 저장
            find.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            find.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:findp')
    else:
        form = FindForm()
    context = {'form': form}
    return render(request, 'pybo/find_form.html', context)

@login_required(login_url='common:login')
def find_delete(request, sale_id):
    find = get_object_or_404(Find, pk=sale_id)
    if request.user != find.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:filddetail', find_id=find.id)
    find.delete()
    return redirect('pybo:findp')