#!/usr/bin/env python
import os

def maxFact(num):
    cnt = num / 2
    while cnt > 1:
        if num % cnt == 0:
            print "largest factor of %d is %d" % (num,cnt)
            break # will escape else statement
        cnt -= 1
    else:
        print num,"is prime,cnt = ",cnt

# list comprehension 
# Generator expression: not create list,use less momery 
def cntNonWhiteCharactor():
    f = open("carddate.txt")
    for eachline in f:
        print repr(eachline)
    # seek the file to re-use the iterator
    f.seek(0)
    # list comprehension
    wordList = [word for line in f for word in line.split()]
    print wordList
    print "word count:",len(wordList)
    f.seek(0)
    #print "non-white charactors:",sum([len(word) for line in f for word in line.split()])
    # Generator expression
    print "non-white charactors:",sum(len(word) for line in f for word in line.split())    
    print "file size:",os.stat("carddate.txt").st_size
    f.close

def yield_expr():
    rows = [1,2,3,4]
    def cols():
        yield 1
        yield 2
        yield 3
    x_product_pairs = ((i,j) for i in rows for j in cols())
    print type(x_product_pairs)
    for pair in x_product_pairs:
        print pair

def creatMatrix(row=3,col=5):
    print [(x+1,y+1) for x in range(row) for y in range(col)]

def findMaxLineListComprehension():
    f = open("carddate.txt")
    allLineLens = [len(x.strip()) for x in f]
    f.close()
    print allLineLens
    print max(allLineLens)

def findMaxLineGenerator():
    f = open("carddate.txt")
    maxLinelen = max(len(x.strip()) for x in f)
    f.close()
    print maxLinelen

def findMaxLineGenerator2():
    maxLinelen = max(len(x.strip()) for x in open("carddate.txt"))
    print maxLinelen

if __name__ == "__main__":
    #for eachnum in range(10,21):
    #    maxFact(eachnum)

    #creatMatrix(row=3,col=5)
    #cntNonWhiteCharactor()
    #yield_expr()
    #findMaxLineListComprehension()
    #findMaxLineGenerator()
    findMaxLineGenerator2()