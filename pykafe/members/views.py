from django.views.generic.edit import UpdateView, DeleteView, CreateView, ModelFormMixin
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from members.models import Member
from rest_framework import viewsets
from members.serializers import MemberSerializer


class List(ListView):
    model = Member
    template_name = 'members/list.html'


class Edit(SuccessMessageMixin, UpdateView):
    model = Member
    fields = ['first_name', 'last_name', 'job_title', 'bio_text', 'photo']
    template_name = 'members/edit.html'
    success_url = reverse_lazy('list')
    success_message = "Updated successfully"


class Delete(DeleteView):
    model = Member
    template_name = 'members/delete.html'
    success_url = reverse_lazy('list')


class Create(SuccessMessageMixin, CreateView):
    model = Member
    fields = ['first_name', 'last_name', 'username', 'password']
    template_name = 'members/create.html'
    success_url = reverse_lazy('list')
    success_message = "Create successfully"

    def form_valid(self, form):
        ''' Overriding the form valid method to set the user password correctly '''
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
