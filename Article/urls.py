from django.conf.urls import url

urlpatterns = [
    url(r'^lists/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
    url(r'^creat/(?P<block_id>\d+)', "article.views.create_article", name="article_create"),
    url(r'^detail/(?P<article_id>\d+)', "article.views.article_detail", name="article_detail"),

]