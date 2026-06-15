class Solution(object):
    def mostCommonWord(self, p, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r'\w+',p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]