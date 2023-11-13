# This is a sample Python script.
import subprocess
import json
from module import pullRequestData, commitData

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def gitClone():
    # クローン元のリポジトリURL
    repository_url = 'https://github.com/NAIST-SE/DevGPT.git'

    # クローン先のディレクトリ
    destination_directory = '/Users/watanabemiku/PycharmProjects/iiii/DevGPT'

    # Gitコマンドを実行してクローン
    try:
        subprocess.check_call(['git', 'clone', repository_url, destination_directory])
        print(f'Repository cloned to {destination_directory}')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')


def readJson(filePath):
    # json.load関数を使ったjsonファイルの読み込み
    with open(filePath) as f:
        di = json.load(f)

    pull_Request_Data = {}
    # Sources内の各要素のAnswerの個数を調べる
    id = 0
    for source in di['Sources']:
        author = source.get('Author', [])
        body = source.get('Body', [])
        # if body=="":
        #     body = 'unknown'
        url = source.get('URL', [])
        chatgpt_sharing = source.get('ChatgptSharing', [])
        for chatgpt in chatgpt_sharing:
            mentions = chatgpt.get('Mention', [])
            mentioned_author = mentions.get('MentionedAuthor', [])
            mentioned_text = mentions.get('MentionedText', [])

            if author != mentioned_author:
                id += 1
                data = pullRequestData.PullRequstData(author, body, mentioned_author, mentioned_text, url)
                pull_Request_Data[id] = data

    allCommit = len(di['Sources'])
    pullResult = commitData.commitData(allCommit, pull_Request_Data)
    return pullResult

    # pullRequestData.toString(value.writeAuthor,value.reviewAuthor,value.body,value.mention)

    # print(di['Sources'][i]['ChatgptSharing'][0]['Conversations'][0]['Answer'])

    # # 'Sources' リスト内の最初の要素の 'ChatgptSharing' セクションを選択
    # chatgpt_sharing = di['Sources'][0]['ChatgptSharing']
    #
    # # 'Answer' フィールドを取得
    # answer = chatgpt_sharing['Conversations'][0]['Answer']
    # print(answer);
    #


# Press the green button in the gutter to run the script.
def db_connect():
    connection = MySQLdb.connect(
        host='127.0.0.1',
        user='me',
        passwd='goma',
        db='pr_commit_db')
    cursor = connection.cursor()


if __name__ == '__main__':
    db_connect();

    fileHead = "DevGPT/"
    filePath = ["snapshot_20230727/20230727_195927_pr_sharings.json",
                "snapshot_20230803/20230803_093947_pr_sharings.json",
                "snapshot_20230810/20230810_123110_pr_sharings.json",
                "snapshot_20230817/20230817_125147_pr_sharings.json",
                "snapshot_20230824/20230824_100450_pr_sharings.json",
                "snapshot_20230831/20230831_060603_pr_sharings.json",
                "snapshot_20230907/20230907_091631_pr_sharings.json",
                "snapshot_20230914/20230914_074826_pr_sharings.json",
                "snapshot_20231012/20231012_233628_pr_sharings.json"]

    result = {}
    for path in filePath:
        result[path] = readJson(fileHead + path)

    for k, data in result.items():
        print("directory : " + k)
        print("allCommit : " + str(data.allCommit))
        print("deferentAuthorCommit : " + str(len(data.pullRequestData)))
        # for value in data.pullRequestData.values():
        #     print("Author:" + value.writeAuthor + "\nMentionedAuthor:" + value.reviewAuthor)
        # print("-------------------------")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
