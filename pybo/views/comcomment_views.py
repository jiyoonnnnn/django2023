from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ComcommentForm
from ..models import Comwrite, Comcomment

@login_required(login_url='common:login')
def comcomment_create(request, comwrite_id):
    comwrite = get_object_or_404(Comwrite, pk=comwrite_id)
    if request.method == "POST":
        form = ComcommentForm(request.POST)
        if form.is_valid():
            comcomment = form.save(commit=False)
            comcomment.author = request.user  # author 속성에 로그인 계정 저장
            comcomment.create_date = timezone.now()
            comcomment.comwrite = comwrite
            comcomment.save()
            return redirect('pybo:detail', comwrite_id=comwrite.id)
        else:
            form = ComcommentForm()
    context = {'comwrite': comwrite, 'form': form}
    return render(request, 'pybo/comwrite_detail.html', context)

@login_required(login_url='common:login')
def comcomment_delete(request, comcomment_id):
    comcomment = get_object_or_404(Comcomment, pk=comcomment_id)
    if request.user != comcomment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comcomment.delete()
    return redirect('pybo:detail', comwrite_id=comcomment.comwrite.id)