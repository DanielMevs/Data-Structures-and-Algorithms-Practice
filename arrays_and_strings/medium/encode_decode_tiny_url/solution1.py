class Codec:

    def __init__(self) -> None:
        # - Long url to short url key, value pair
        self.encodeMap = {}
        # - Short url to long url key, value pair
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
            return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.decodeMap[shortUrl]
        