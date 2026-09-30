class Twitter:

    def __init__(self):
        self.followingList = defaultdict(set)
        self.tweets = []        
        self.tweetTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((-self.tweetTime, userId, tweetId))
        self.tweetTime += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed_raw = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if len(feed_raw) == 10:
                break
            if self.tweets[i][1] == userId or self.tweets[i][1] in self.followingList[userId]:
                heapq.heappush(feed_raw, self.tweets[i])

        res = []
        while feed_raw:
            res.append(heapq.heappop(feed_raw)[2])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingList[followerId]:
            self.followingList[followerId].remove(followeeId)
        
