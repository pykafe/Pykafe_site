from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from members.models import Member


class List(ListView):
    model = Member
    template_name = 'members/list.html'
    
    
class Edit(UpdateView):
    model = Member
    fields = ['first_name', 'last_name', 'job_title', 'bio_text', 'photo']
    template_name = 'members/edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        return super(Edit, self).dispatch(request, *args, **kwargs)
        

class Delete(DeleteView):
    model = Member
    template_name = 'members/delete.html'
    success_url = reverse_lazy('list')
