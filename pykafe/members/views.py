from django.views.generic.edit import UpdateView, DeleteView, CreateView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from members.models import Member
from endless_pagination.views import AjaxListView
from haystack.views import SearchView as HayStackSearchView
from members.forms import PykafeSearchForm


class List(AjaxListView, HayStackSearchView):
    model = Member
    template_name = 'members/list.html'
    page_template = 'members/list_page.html'
    form_class = PykafeSearchForm
    allow_emty = True
    load_all = True
    searchqueryset = None

    def get_queryset(self, *args, **kwargs):
        self.form = self.build_form()
        self.query = self.get_query()
        return self.get_results()

    def get_context_data(self, *args, **kwargs):
        context = super(List, self).get_context_data(*args, **kwargs)
        context['search_form'] = self.form_class
        return context


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
