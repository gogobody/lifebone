from users.models import User
user1 = User(name="enen", password="123")
user1.save()
user2 = User(name="dala", password="123")
user2.save()
user_list = User.objects.all()
print user_list
