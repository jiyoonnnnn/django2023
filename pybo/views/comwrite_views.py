from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ComwriteForm
from ..forms import Comwrite

@login_required(login_url='common:login')
def comwrite_create(request):
    if request.method == 'POST':
        form = ComwriteForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            comwrite = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            comwrite.author = request.user  # author 속성에 로그인 계정 저장
            comwrite.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            comwrite.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:guicom')
    else:
        form = ComwriteForm()
    context = {'form': form}
    return render(request, 'pybo/comwrite_form.html', context)

@login_required(login_url='common:login')
def comwrite_modify(request, comwrite_id):
    comwrite = get_object_or_404(Comwrite, pk=comwrite_id)
    if request.user != comwrite.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', comwrite_id=comwrite.id)
    if request.method == "POST":
        form = ComwriteForm(request.POST, instance=comwrite)
        if form.is_valid():
            comwrite = form.save(commit=False)
            comwrite.modify_date = timezone.now()  # 수정일시 저장
            comwrite.save()
            return redirect('pybo:detail', comwrite_id=comwrite.id)
    else:
        form = ComwriteForm(instance=comwrite)
    context = {'form': form}
    return render(request, 'pybo/comwrite_form.html', context)

@login_required(login_url='common:login')
def comwrite_delete(request, comwrite_id):
    comwrite = get_object_or_404(Comwrite, pk=comwrite_id)
    if request.user != comwrite.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', comwrite_id=comwrite.id)
    comwrite.delete()
    return redirect('pybo:guicom')