# This is a sample Python script.
import subprocess
import json
from module import pullRequestData, commitData,deleteMatchPull
import mysql.connector

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

    Request_Data = {}
    # Sources内の各要素のAnswerの個数を調べる
    id = 0
    for source in di['Sources']:
        author = source.get('Author', [])
        create_time = source.get('CreatedAt', [])
        body = source.get('Body', [])
        body = body[:1000]

        # if body=="":
        #     body = 'unknown'
        url = source.get('URL', [])
        chatgpt_sharing = source.get('ChatgptSharing', [])
        for chatgpt in chatgpt_sharing:
            mentions = chatgpt.get('Mention', [])
            mention_time = chatgpt.get('DateOfConversation', [])
            mention_time = str(mention_time)
            mention_time = mention_time.replace(",","")

            mentioned_author = mentions.get('MentionedAuthor', [])
            text = mentions.get('MentionedText', [])
            mentioned_text = text[:1000]

            if author != mentioned_author:
                id += 1
                data = pullRequestData.PullRequstData(author, body, mentioned_author, mentioned_text, url,create_time,mention_time)
                Request_Data[id] = data

    allCommit = len(di['Sources'])
    pullResult = commitData.commitData(allCommit, Request_Data)
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

def creatTable(cursor):
    # 初期
    cursor.execute("DROP TABLE IF EXISTS pr_commit_list")
    try:
        # テーブルの作成
        cursor.execute("""CREATE TABLE pr_commit_list(
                       id INT(11) AUTO_INCREMENT NOT NULL,
                       directory VARCHAR(1000) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       author VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       createtime VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       mentiontime VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       reviewer varchar(100) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       body VARCHAR(5000) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       mention VARCHAR(5000) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       url VARCHAR(1000) NOT NULL COLLATE utf8mb4_unicode_ci , 
                       PRIMARY KEY (id)
                       )""")
    except Exception as e:
        print(f"Error creating table: {e}")
def addDataBase(cursor, directory, author, reviewer, body, mention , url,create_time,mention_time):
    # Add data
    sql = "INSERT INTO pr_commit_list(directory, author, createtime,mentiontime, reviewer, body, mention, url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (directory, author, create_time,mention_time,reviewer, body, mention , url))
    connection.commit()


def deleteSamecommit(json_dict):
    validator = set()
    distinct_PRs = []
    for _, pre_value in json_dict.items():
        for _, p_value in pre_value.Request_Data.items():
            if p_value.get_string() in validator:
                # print("already exist")
                pass
            else:
                distinct_PRs.append(p_value)
                validator.add(p_value.get_string())
    return distinct_PRs

if __name__ == '__main__':

    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='me',
        passwd='goma',
        db='pr_commit_db')
    cursor = connection.cursor()

    creatTable(cursor)

    fileHead = "../DevGPT/"
    filePath = ["snapshot_20230727/20230727_195927_pr_sharings.json",
                "snapshot_20230803/20230803_093947_pr_sharings.json",
                "snapshot_20230810/20230810_123110_pr_sharings.json",
                "snapshot_20230817/20230817_125147_pr_sharings.json",
                "snapshot_20230824/20230824_100450_pr_sharings.json",
                "snapshot_20230831/20230831_060603_pr_sharings.json",
                "snapshot_20230907/20230907_091631_pr_sharings.json",
                "snapshot_20230914/20230914_074826_pr_sharings.json",
                "snapshot_20231012/20231012_233628_pr_sharings.json"]

    json_dict = {}
    for path in filePath:
        json_dict[path] = readJson(fileHead + path)

    PRs = deleteSamecommit(json_dict)
    print(len(PRs))
    for pr in PRs:
        print(pr.get_string())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
