from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['article', 'name', 'image', 'message']
        exclude = ['article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'file',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'cols': '30',
            'rows': '10',
            'id': 'message',
        })

