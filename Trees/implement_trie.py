'''
https://leetcode.com/problems/implement-trie-prefix-tree/
208. Implement Trie (Prefix Tree)
Medium

===

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

===

'''

class TrieNode:
    def __init__(self):
        self.isWord = False;
        self.children = [None for i in range(26)];
        self.numWords = 0;

class Trie:

    def __init__(self):
        self.root = TrieNode();

    def insert(self, word: str) -> None:
        if self.search(word):
            return;
        
        c = self.root;
        i = 0;

        while i < len(word):
            idx = ord(word[i])-97;
            if c.children[idx] == None:
                c.children[idx] = TrieNode();
            
            c.numWords += 1;
            c = c.children[idx];
            i += 1;

        c.numWords += 1;
        c.isWord = True;

    def search(self, word: str) -> bool:
        c = self.root;
        i = 0;

        while i < len(word):
            idx = ord(word[i])-97;
            if c.children[idx] == None:
                return False;

            c = c.children[idx];
            i += 1;
        
        return c.isWord;

    def startsWith(self, prefix: str) -> bool:
        c = self.root;
        i = 0;

        while i < len(prefix):
            idx = ord(prefix[i])-97;
            if c.children[idx] == None:
                return False;

            c = c.children[idx];
            i += 1;
        
        if c.numWords > 0:
            return True;
        return False;


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)