from django import forms
from core.models import User
from userfollows.models import UserFollows


class UserForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs["user"]
        del kwargs["user"]
        super().__init__(*args, **kwargs)
        self.fields["user_list"] = forms.ModelChoiceField(
            to_field_name="username",
            queryset=self.get_users_list())

    def get_users_list(self):
        fe = UserFollows.objects.filter(user=self.user) 
        return (User.objects.all().order_by("username")
                .exclude(pk=self.user.id)
                .exclude(
                    pk__in=[User.objects.get(id=e.followed_user_id).id for e in fe] 
                ))
