# Find a users latest tweet and their oldest tweet

"//Find 1st, Find Nth"

arr = [{'tweet':'hi','date':2021},
       {'tweet':'teddy','date':2014},
       {'tweet':'my','date':2022}]

def get_entry(arr):
    oldest_tweet = arr[0]
    latest_tweet = arr[0]

    for i in range(1,len(arr)):
        tweet = arr[i]
        if tweet['date'] < oldest_tweet['date']:
            oldest_tweet = tweet
            continue
        
        if tweet['date'] > latest_tweet['date']:
            latest_tweet = tweet
            continue
    return f'Latest tweet: {latest_tweet["tweet"]}, Oldest tweet:{oldest_tweet["tweet"]}'
        
    

result = get_entry(arr)
print(result)

#NOTE for the get_entry function we can conclude that the worst-case performance is O(n^2). Solved with O(n).