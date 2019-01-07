from django.shortcuts import render
from django.views.generic import TemplateView


class BlogHomeView(TemplateView):
    template_name = 'blog/home.html'

class PublishPostView(TemplateView):
    template_name = 'blog/publish_post.html'

