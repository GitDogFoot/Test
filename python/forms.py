from .models import Post, Category
from django import forms
# from django_summernote.widgets import SummernoteWidget
from froala_editor.widgets import FroalaEditor


class PostForm(forms.ModelForm):
  # content = forms.TextInput(widget=FroalaEditor)

  class Meta:
    model = Post
    fields = ['title', 'category', 'content']
    widgets = {
      'content': FroalaEditor,
    }

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'textInput form-control form_title', 'placeholder': '제목을 입력하세요'})
    self.fields['category'].widget.attrs.update({'class': 'form-select form-control form_category'})

