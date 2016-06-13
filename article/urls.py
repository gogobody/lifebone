from django.conf.urls import url


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)$', "article.views.article_list", name="article_list"),
    url(r'^create/(?P<block_id>\d+)/$', "article.views.create_article", name="create_article"),
    url(r'^detail/(?P<article_id>\d+)/$', "article.views.article_detail", name="article_detail"),
]
