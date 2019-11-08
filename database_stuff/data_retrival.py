import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['reddit_speedrun']
comments_collection = db['comments']

def dfs(depth, parent_id):
    comments = comments_collection.find({'parent_id': parent_id})
    # print(comments.explain())
    for comment in comments:
        for i in range(depth):
            print('>', end=' ')
        print('{')
        for i in range(depth):
            print('\t', end='')
        print('body: ', comment['body'])
        for i in range(depth):
            print('\t', end='')
        print('author: ', comment['author'])
        for i in range(depth):
            print('\t', end='')
        print('score: ', comment['score'])
        for i in range(depth-1):
            print('\t', end='')
        print('}')
        dfs(depth+1, 't'+str(depth)+'_'+str(id))

# dfs(1, 't3_3fcrpe')

subs = []
submissions_collection = db['submissions']
submissions = submissions_collection.find({})
for submission in submissions:
    sub_dict = {}
    if 'permalink' in submission:
        sub_dict['permalink'] = submission['permalink']
    if 'selftext' in submission:
        sub_dict['selftext'] = submission['selftext']
    if 'author_flair_text' in submission:
        sub_dict['author_flair_text'] = submission['author_flair_text']
    sub_dict['title'] = submission['title']
    