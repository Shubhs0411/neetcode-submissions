class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #cat->bat->bag->sag
        #edge cases:
        #if empty beginWord and endWord or no WordList e=return 0 
        #if one Word(endWord) in wordList, 2
        #beginWord in wordList, fine
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        adj=defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern=w[:i]+"*"+w[i+1:]
                adj[pattern].append(w)
        
        q=deque()
        visit=set()
        q.append(beginWord)
        visit.add(beginWord)
        res=1

        while q:
            
            for _ in range(len(q)):
                c=q.popleft()
                if c==endWord:
                    return res
                for i in range(len(c)):
                    pattern=c[:i]+"*"+c[i+1:]
                    for w in adj[pattern]:
                        if w not in visit:
                            q.append(w)
                            visit.add(w)
            res+=1
        return 0
                    
#beginWord="cat", endWord="sag", wordList=["bat", "bag, "sag"], output=4
#q=(cat, bat, bag, sag)
#adj={*at:[cat,bat],
#c*t:[cat],
#ca*:[cat],
#b*t:[bat],
#ba*:[bat,bag],
#*ag:[bag, sag],
#b*g:[bag],
#s*g:[sag]
#}
#visit=[cat, bat,bag,sag]
#res=1+1+1+1=4

        