class Post:
    def __init__(self, id, type, author, avatar, time):
        self.id = id
        self.type = type
        self.author = author
        self.avatar = avatar
        self.time = time
        self.comments = []

    def addComment(self, comment):
        self.comments.append(comment)


class TextPost(Post):
    def __init__(self, id, type, author, avatar, time, text):
        super().__init__(id, type, author, avatar, time)
        self.text = text

class PhotoPost(Post):
    def __init__(self, id, type, author, avatar, time, photo, alt, title):
        super().__init__(id, type, author, avatar, time)
        self.photo = photo
        self.alt = alt
        self.title = title

class VideoPost(Post):
    def __init__(self, id, type, author, avatar, time, video, poster):
        super().__init__(id, type, author, avatar, time)
        self.video = video
        self.poster = poster

class Comment():
    def __init__(self, id, postID, avatar, name, text):
        self.id = id
        self.postID = postID
        self.avatar = avatar
        self.name = name
        self.text = text