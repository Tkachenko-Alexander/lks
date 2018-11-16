from django.views.generic import DetailView, ListView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render_to_response, render
from .models import Article
from .serializers import ArticleSerializer
from apps.contacts.forms.subscribe import SubscribeForm
from django.conf import settings


class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class BlogListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['form_subscribe'] = SubscribeForm()
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'


# def handler404(request, exception, template_name="httpresponse/404.html"):
#     response = render_to_response("httpresponse/404.html")
#     response.status_code = 404
#     return response

def error_404(request, exception):
    return render(request, 'httpresponse/404.html', status=404)