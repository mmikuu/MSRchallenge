from module import pullRequestData
class PullRequstData:

    def __init__(self, author,body,review_author,mention,url,create_time,mention_time):
        self.writeAuthor = author
        self.reviewAuthor = review_author
        self.body = body
        self.mention = mention
        self.url = url
        self.create_time = create_time
        self.mention_time = mention_time

    def printString(self):
        print(self.get_string())

    def get_string(self):
        return "Author:" + self.writeAuthor +"\nMentionedAuthor:" + self.reviewAuthor + "\nBody:" + self.body + "\nmention" + self.mention





