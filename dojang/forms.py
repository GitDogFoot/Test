from .models import Post, Category, Subject
from django import forms
from froala_editor.widgets import FroalaEditor


class PostForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor)

  class Meta:
    model = Post
    fields = ['title', 'category', 'subject']

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'textInput form-control form_title', 'placeholder': '제목을 입력하세요'})
    self.fields['category'].widget.attrs.update({'class': 'form-select form-control form_category'})
    self.fields['subject'].widget.attrs.update({'class': 'form-select form-control form_subject'})

