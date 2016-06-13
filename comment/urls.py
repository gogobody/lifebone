from django.conf.urls import url


urlpatterns = [
    url(r'^create/$', "comment.views.create_comment", name="create_comment"),
    url(r'^list/$', "comment.views.comment_list", name="comment_list"),
]
