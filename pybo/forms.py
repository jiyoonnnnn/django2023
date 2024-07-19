from django import forms
from pybo.models import Comwrite, Comcomment, Sale, Find


class ComwriteForm(forms.ModelForm):
    class Meta:
        model = Comwrite  # 사용할 모델
        fields = ['subject', 'content']  # ComwriteForm에서 사용할 Comwrite 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale  # 사용할 모델
        fields = ['subject', 'content']  # ComwriteForm에서 사용할 Comwrite 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class FindForm(forms.ModelForm):
    class Meta:
        model = Find # 사용할 모델
        fields = ['subject', 'content',]  # ComwriteForm에서 사용할 Comwrite 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class ComcommentForm(forms.ModelForm):
    class Meta:
        model = Comcomment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }