# encoding: utf-8
from uuid import uuid4

class User(object):
    LIMIT = 50
    
    def __init__(self, uuid, full_name):
        self.full_name = full_name
        self.uuid = uuid # uuid4()
        self.post = [None] * self.LIMIT
        self.post_index = 0

    def add_post(self, post):
        self.posts[self.post_index] = post
        self.post_index = (self.post.index + 1) % self.LIMIT    
    

    def get_post(self):
        for post in self.post:
            yield post

        # second way to do so return iter(self.post)
        # return (post for post in self.posts)


class Post(object):
    def __init__(self, id, user_id, content):
        self.id = id
        self.user_id = user_id
        self.content = content
