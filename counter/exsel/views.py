from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import ProductForm
from .models import Product, Rubric


class HomePageView(CreateView):
	form_class = ProductForm
	template_name = 'home.html'
	success_url = reverse_lazy('home')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['all_products_list'] = Product.objects.all()
		context['all_rubrics_list'] = Rubric.objects.all()
		return context
