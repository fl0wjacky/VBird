#! /usr/bin/env python
# coding:utf-8

import sys

stops = ' ！，。'
stops = stops.decode('utf-8')

def getLength(poe):
    situation = [i for i in range(len(poe)) if poe[i] in stops] 
    situation.insert(0, -1)
    print situation
    gaps = [situation[i] - situation[i - 1] for i in range(1, len(situation))]
    print gaps
    if gaps:
        return max(gaps)
    else:
        return None

def transferPoetry(poe, sentLength):
    NewPoe = []
    tempSent = []
    for i in poe:
        if i not in stops:
            tempSent.append(i)
        elif len(tempSent) < sentLength:
            tempSent += stops[0] * (sentLength - len(tempSent))
            NewPoe.append(tempSent)
            tempSent = []
    return NewPoe 
    
if __name__ == '__main__':
    poe = raw_input('Please input your poetry:')
    poe = poe.decode('utf-8')
    print('the poetry is: %s' % poe)
    print('the length is %d' % len(poe))
    sentLength = getLength(poe)
    if sentLength:
        print transferPoetry(poe, sentLength)
    else:
        print 'Are you sure this is a poetry???'
