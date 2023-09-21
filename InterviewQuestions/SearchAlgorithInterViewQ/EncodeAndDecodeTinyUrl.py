# Encode and Decode TinyUrl

"""
Tiny Url is a URL shorting service where you enter a URL such as "https://leetcode.com/problems/design-tinyurl" and it returns a
short URL such as "http://tinyurl.com/4e91Ak". Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorith should work. You just need to ensure that a URL can be encoded to a tiny URL
and the tiny URL can be decoded to the original URL.

implement the "Solution" class:
    Solution() initializes the object of the system.
    String encode(String longUrl) Returns a tiny URL for the given longUrl.
    String decode(String shortUrl) Returns the original long Url for the given shortUrl. it is guaranteed that the given
    shortUrl was encoded by the same object.

Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https//leetcode.com//problems/design-tinyurl"

Explanation:
Solution obj = new Solution()
string tiny = obj.encode(); // returns the encoded tiny url.
string ans = obj.decode(); // return the original url after decoding it.

"""


class Solution:
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodingMap[shortUrl]


sol = Solution()
print(sol.encode("https://alnilamclothing.com/test/test/test"))
print(sol.decode("https://tinyurl.com/1"))