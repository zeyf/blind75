'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/
211. Design Add and Search Words Data Structure
Medium

===

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 10^4 calls will be made to addWord and search.

===

First idea:
    - Treat it like a regular trie on insertion.
    - Treat it like a regular trie on the NO PERIODS word searches.
    - On searches WITH PERIODS, try any valid child when word[k] == '.'
        - if word[k] != '.', check if a specific child (ord(word[k])-97) is found.
            - if found, keep traversing, else return False.
        - when k == len(str), if the isWord flag of a given node is on, return True.
            - LOGICAL OR this result with a res = False variable. The true answer will bubble up after traversing the whole structure.
'''

class WordDictionaryNode:
    def __init__(self):
        self.isWord = False;
        self.children = [None for i in range(26)];

class WordDictionary:

    def __init__(self):
        self.root = WordDictionaryNode();
        self.words = set();

    def addWord(self, word: str) -> None:
        if word in self.words:
            return;
        c, i = self.root, 0;

        while i < len(word):
            idx = ord(word[i])-97;
            if c.children[idx] == None:
                c.children[idx] = WordDictionaryNode();
            
            c = c.children[idx];
            i += 1;
        
        c.isWord = True;
        self.words.add(word);

    def search(self, word: str) -> bool:

        foundPeriod, i = False, 0;
        while i < len(word) and not foundPeriod:
            if word[i] == '.':
                foundPeriod = True;
            i += 1;
        if not foundPeriod:
            return word in self.words;

        return self.searcher(self.root, word, 0, "");

    def searcher(self, node, searchWord, k, string):
        if k == len(searchWord):
            return node.isWord;
        
        res, idx = False, ord(searchWord[k])-97;

        if searchWord[k] != '.':
            if node.children[idx] == None:
                return False;
            else:
                res = self.searcher(node.children[idx], searchWord, k + 1, string + searchWord[k]);
        else:
            i = 0;
            while i < 26 and not res:
                if node.children[i] != None:
                    res = res or self.searcher(node.children[i], searchWord, k + 1, string + chr(97+i));
                i += 1;
        return res;