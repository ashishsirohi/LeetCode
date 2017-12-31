from collections import defaultdict
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        tmpList = sorted(self.tweets[userId], key=lambda x: x[1], reverse=True)
        if len(tmpList) > 10:
            result.append(tmpList[:10])
        else:
            result.append(tmpList)
        del tmpList[:]
        for follower in defaultdict[userId]:
            tmpList = sorted(self.tweets[follower], key=lambda x: x[1], reverse=True)
            if len(tmpList) > 10:
                result.append(tmpList[:10])
            else:
                result.append(tmpList)

        print result


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followers[followerId]:
            self.followers[followeeId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)