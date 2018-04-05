#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#

"""
File: wordladder单词变换.py
Author: dsgdtc@163.com
Date: 2017/12/26 20:35
给定字典和一个起点单词，一个终点单词，每次只能变换一个字母，问从起点单词是否能够到达终点单词，最短多少步

单元点的最短路径问题，能通过一个字母变换而得到的单词，认为有边。
最短，最小往往使用bfs
"""
class SolutionA(object):

    def __init__(self):
        pass

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # wordList当做队列数据结构
        wordList = wordList
        visited = set()
        visited.add(beginWord)
        wordList.append(endWord)
        depth = 1

        while endWord not in visited:
            temp = set()
            for word in visited:
                print("Checking word is: %s" %(word))
                for i in range(len(word)):
                    chars = list(word)
                    print("Split it to chars %s" %(chars))
                    input("enter to coninue...")
                    for j in range(ord('a'), ord('z') + 1):
                        chars[i] = chr(j)
                        newWord = ''.join(chars)
                        print("newWord is %s, j is: %s" %(newWord, chr(j)))
                        if newWord in wordList:
                            print ("newWord %s is in wordList %s" %(newWord, wordList))
                            temp.add(newWord)
                            wordList.remove(newWord)
                            print ("temp is %s wordList is %s" %(temp, wordList))
                            input("etc...")

            depth += 1
            if len(temp) == 0: # if 0, it never gets to the endWord
                return 0
            # 循环一次后,visited里是当前层的节点
            visited = temp
            print ("111111111111111111111111visited: %s, depth is %s, endworld is %s" %(visited, depth, endWord))
            input("etc...")

        return depth

class SolutionB(object):

    def __init__(self):
        pass
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        q = [(beginWord,1)]

        while q:
            e, lens = q.pop(0)
            print (e, lens)
            input('enter to continue...')
            if e == endWord:
                return lens
            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]
                print ("left is %s" %(left))
                print ("right is %s" %(right))
                input("enter to continue...")
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right
                        if nextWord in wordList:
                            print (nextWord)
                            q.append((nextWord, lens + 1))
                            wordList.remove(nextWord)
        return 0



if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print (beginWord, endWord, wordList)
    s = SolutionA()
    res = s.ladderLength(beginWord, endWord, wordList)
    print (res)