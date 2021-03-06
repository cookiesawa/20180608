from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required

# Create your views here.




#--- TemplateView
class HomeView(TemplateView):
    template_name = '../templates/post/post_list.html'

#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)