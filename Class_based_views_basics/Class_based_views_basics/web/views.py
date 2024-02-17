from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render

from Class_based_views_basics.web.models import TodoList


# Create your views here.
class IndexRawView(views.View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'web/index.html')

    def post(self, request):
        pass

class IndexView(views.TemplateView):
    template_name = 'web/index.html'

    extra_context = {
        'title': 'First class based template view with extra content',
        "static_time": datetime.now()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        context['todo_list'] = TodoList.objects.all()

        return context

class TodoListDetailsView(views.DetailView):
    model = TodoList
    template_name = 'web/details.html'
    def get_queryset(self):
        return super().get_queryset().filter(title__icontains='work')


class TodoListCreateView(views.CreateView):
    model = TodoList
    fields = '__all__'
    template_name = 'web/create_todo.html'
    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('todo_details', kwargs={'pk': 1})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['deadline'].widget.attrs['type'] = 'date'
        form.fields['deadline'].widget.attrs['class'] = 'form-control'
        form.fields['title'].widget.attrs['placeholder'] = 'Enter title here'
        form.fields['deadline'].widget.attrs['placeholder'] = 'deadline in format YYYY-MM-DD'

        return form

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = TodoList.objects.all()
        return context


