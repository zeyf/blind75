'''
https://leetcode.com/problems/word-search-ii/
212. Word Search II
Hard

===

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

===

First idea:
    - Use a Trie (numWords variant) to word search. As long as numWords of adding a character is > 0, continue traversing.


'''

class TrieNode:
    def __init__(self):
        self.numWords = 0;
        self.isWord = False;
        self.children = [None for i in range(26)];


class Trie:
    def __init__(self):
        self.root = TrieNode();
        self.wordPool = {  };
    
    def insert(self, word):
        if self.search(word):
            return;

        c = self.root;
        for char in word:
            if c is not self.root:
                c.numWords += 1;
            
            idx = ord(char)-97;
            if c.children[idx] == None:
                c.children[idx] = TrieNode();
            c = c.children[idx];
        
        c.numWords += 1;
        c.isWord = True;
        self.wordPool[word] = c;
    
    def search(self, word):
        return word in self.wordPool;
    
    def getPrefixNode(self, word):
        c = self.root;

        for char in word:
            idx = ord(char)-97;
            if c.children[idx] == None:
                return None;
            c = c.children[idx];

        return c;

class Solution:

    def __init__(self):
        self.dr = [-1,0,0,1];
        self.dc = [0,-1,1,0];

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie();
        for word in words:
            t.insert(word);
        
        n, m = len(board), len(board[0]);
        visited = set();
        found = set();
        for row in range(n):
            for col in range(m):
                searchres = t.getPrefixNode(board[row][col]);
                if searchres:
                    self.dfs(board, n, m, row, col, visited, searchres, "", t, found);
        
        return [foundWord for foundWord in found];
    
    def inbounds(self, n, m, row, col):
        return not (row < 0 or col < 0 or row >= n or col >= m);
                
    def dfs(self, board, n, m, row, col, visited, node, string, trie, found):

        string += board[row][col];
        visited.add((row, col));

        for i in range(4):
            nr, nc = row + self.dr[i], col + self.dc[i];
            if self.inbounds(n, m, nr, nc) and (nr, nc) not in visited:
                searchresNext = node.children[ord(board[nr][nc])-97];
                if searchresNext and searchresNext.numWords > 0:
                    self.dfs(board, n, m, nr, nc, visited, searchresNext, string, trie, found);

        visited.remove((row, col));
        if node and node.isWord:
            found.add(string);

        
