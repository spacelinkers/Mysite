from django.urls import path

from blog.views import BlogHomeView,PublishPostView

app_name = 'blog'
urlpatterns = [
    path('', BlogHomeView.as_view(), name = 'blogHome'),
    path('publish/', PublishPostView.as_view(), name = 'publish_post'),
    
]