from module import pullRequestData
class PullRequstData:

    def __init__(self, author,body,review_author,mention,url):
        self.writeAuthor = author
        self.reviewAuthor = review_author
        self.body = body
        self.mention = mention
        self.url = url

    def printString(self,author,review_author,body,mention):
        print("Author:" + author +"\nMentionedAuthor:" + review_author + "\nBody:" + body + "\nmention" + mention)





