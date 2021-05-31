from mongoengine import *
import datetime

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

connect('mongoengine_test', host='localhost', port=27017)
post_1 = Post(title='Sample Post',content='Some engaging content',author='Scott')
post_1.save()

post_2 = Post(title="Good title", content='Content goes here', author='David')
post_2.save()

for post in Post.objects:
    print()
    print("Title:" + post.title)
    print("Content:" + post.content)
    print("Author:" + post.author)



