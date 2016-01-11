from django.utils.translation import ugettext_lazy as _
from django import forms
from haystack.forms import SearchForm

from members.models import Member


class PykafeSearchForm(SearchForm):

    q = forms.CharField(label="", max_length=128, required=False)

    username = forms.ModelChoiceField(queryset=Member.objects.all(), empty_label=_('All Users'))

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', 'search_%s')
        super(PykafeSearchForm, self).__init__(*args, **kwargs)

    def search(self):

        self.is_bound = True
        self.full_clean()

        # First, store the SearchQuerySet received from other processing.
        if self.cleaned_data['q'] != '':
            search_queryset = self.searchqueryset.auto_query(self.cleaned_data['q'])
        else:
            search_queryset = self.searchqueryset

        # Check to see if a assigned was chosen.
        if 'username' in self.cleaned_data:
            search_queryset = search_queryset.filter(username=self.cleaned_data['username'])

        if 'first_name' in self.data:
            search_queryset = search_queryset.order_by('first_name')

        if 'last_name' in self.data:
            search_queryset = search_queryset.order_by('last_name')

        if 'job_title' in self.data:
            search_queryset = search_queryset.order_by('job_title')

        return search_queryset
