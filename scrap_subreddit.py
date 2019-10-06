def scrap_subreddit(scrapped_data, subreddit, obj):

    try:
        if obj['subreddit'] == subreddit:
            # print(obj)
            scrapped_data.append(obj)
    except Exception as e:
        pass
