from django.views.generic.edit import UpdateView
from members.models import Member

class Edit(UpdateView):
    model = Member
    fields = ['job_title', 'bio_text', 'photo']
    template_name = 'members/edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        return super(Edit, self).dispatch(request, *args, **kwargs)

