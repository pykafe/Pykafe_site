from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login


class Home(TemplateView):
    template_name = 'members/index.html'


class Login(TemplateView):
	template_name = 'members/login.html'

	def post(self, request, *agrs, **kwargs):

		context = self.get_context_data()

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			response = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		else:
			context['login_failed'] = True
			response = super(TemplateView, self).render_to_response(context)

		return response

