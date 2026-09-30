class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweetTime, userId, tweetId))
        self.tweetTime += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        hp = []
        self.following[userId].add(userId)
        for followingUser in self.following[userId]:
            for tweet in self.tweets[followingUser]:
                heapq.heappush(hp, tweet)
        self.following[userId].remove(userId)

        while len(feed) < 10 and hp:
            feed.append(heapq.heappop(hp)[2])

        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
