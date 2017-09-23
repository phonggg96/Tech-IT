from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from home.models import Comment, TinTuc


class LoginFrom(ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


class CommentForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(MyClassForm, self).__init__(*args, **kwargs)
    #     if 'dropdown1' in self.data:
    #         self.fields['dropdown2'].queryset = Department.objects.filter(typeofcriteria=self.data['dropdown1'])
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__()
        if 'user_id' in self.data:
            self.fields['user'].queryset = User.objects.get(pk=self.data["user_id"])

        if 'post_id' in self.data:
            self.fields['post'].queryset = TinTuc.objects.get(pk=self.data["post_id"])

    class Meta:
        model = Comment
        fields = ("content", )

        widgets = {
            'content': Textarea(attrs={"class": "input"})
        }