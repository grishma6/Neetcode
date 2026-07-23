from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(sorted(words))

        return [item for item, count in counter.most_common(k)]