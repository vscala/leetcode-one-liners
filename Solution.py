'''
  August 2021 LeetCode Daily Challenges: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/
'''
class Solution:
    '''
      Problem: https://leetcode.com/problems/making-a-large-island/
      Solution description: ???
      Complexity: ???
    '''
    #largestIsland = lambda s, g, i=0: max('''cur loc, next loc''') if i < len(grid)*len(grid[0]) else 0
    
    '''
      Problem: https://leetcode.com/problems/two-sum/
      Solution description: A recusive O(n^2) approach that iterates though each pair of elements in the array until a solution is found
      Complexity: Time O(n^2)
    '''
    twoSum = lambda s,n,t,i=0: [i+1+n[i+1:].index(t-n[i]), i] if t-n[i] in n[i+1:] else s.twoSum(n,t,i+1)

    
    '''
      Problem: https://leetcode.com/problems/stone-game/
      Solution desciption: Program output always True regardless of input values
      Complexity: Time O(1), Space O(1)
    '''
    stoneGame = lambda *_ : True
