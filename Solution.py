'''
  A collection of solutions for leetcode problems that can fit in one-line of python
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
      Problem: https://leetcode.com/problems/reverse-integer/
      Solution description: First call of reverse calculates the reverse of integer x, second call checks that the reverse is in bounds and returns 0 if not
    '''
    reverse = lambda s, x, r=False: x * (abs(x) < 2**31) if r else s.reverse([-1,1][x>0]*int((str(abs(x))[::-1])), True)

    '''
      Problem: https://leetcode.com/problems/stone-game/
      Solution desciption: Program output always True regardless of input values
      Complexity: Time O(1), Space O(1)
    '''
    stoneGame = lambda *_ : True

    '''
      Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
      Solution description: Recursively search through a tree until a node is found such that both nodes p and q are neither both less than said node of both greater
      Complexity: Time O(log(n))
    '''
    lowestCommonAncestor = lambda f, c, p, q: f.lowestCommonAncestor(c.right, p, q) if (c.val < p.val and c.val < q.val) else (f.lowestCommonAncestor(c.left, p, q) if (c.val > p.val and c.val > q.val) else c)

    '''
      Problem: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
      Solution description: Increase l until a >= na (https://oeis.org/A300758)
      Complexity: ???
    '''
    minimumPerimeter = lambda s, na, l=0, a=0: l*8 if a>=na else s.minimumPerimeter(na, l+1, a+12*(l+1)**2)
    
    '''
      Problem: https://leetcode.com/problems/build-array-from-permutation/
      Solution: Simply return array of elements at the A[ith] location for each in A
      Complexity: Time O(n) (one pass)
    
    '''
    buildArray = lambda s, A : [A[i] for i in A]
