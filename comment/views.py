# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from article.models import Article
from message.models import UserMessage
from models import Comment
from utils.response import json_response


@login_required
def create_comment(request):
    article_id = int(request.POST["article_id"])
    to_comment_id = int(request.POST["to_comment_id"])
    content = request.POST["content"].strip()

    article = Article.objects.get(id=article_id)
    comment = Comment(block=article.block, article=article,
                      owner=request.user, to_comment_id=to_comment_id,
                      content=content)
    comment.save()
    if to_comment_id == 0:
        new_msg = UserMessage(owner=article.owner,
                              content=u"有人评论了您的文章《%s》" % article.title,
                              link=reverse("article_detail", args=[article.id]))
        new_msg.save()
    else:
        to_comment = Comment.objects.get(id=to_comment_id)
        new_msg = UserMessage(owner=to_comment.owner,
                              content=u"有人回复了你的评论'%s'" % to_comment.content[:30],
                              link=reverse("article_detail", args=[article.id]))
        new_msg.save()
    return json_response({})


@login_required
def comment_list(request):
    pass
