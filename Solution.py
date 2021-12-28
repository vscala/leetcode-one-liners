'''
  A collection of solutions for leetcode problems that can fit in one-line of python
'''
class Solution:
    '''
      Problem: https://leetcode.com/problems/two-sum/
      Solution description: A recusive O(n^2) approach that iterates though each pair of elements in the array until a solution is found
      Complexity: Time O(n^2)
    '''
    twoSum = lambda s,n,t,i=0: [i+1+n[i+1:].index(t-n[i]), i] if t-n[i] in n[i+1:] else s.twoSum(n,t,i+1)
    
    '''
      Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
      Compleixty: Time O(n) (one pass)
    '''
    twoSum_ = lambda s, a, t, l=0, r=-1: s.twoSum(a, t, l+1, r) if a[l] + a[r] < t else (s.twoSum(a, t, l, r-1) if  a[l] + a[r] > t else [l+1, len(a)+r+1])
    
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
    
    '''
      Problem: https://leetcode.com/problems/di-string-match/
      Solution: Iterate over s and return l:=l+1 if s[i] == "I" and r:=r-1 otherwise
      Complexity: Time O(n) (one pass)
    '''
    diStringMatch = lambda t, s, l=-1, r=0: [(l:=l+1) if s[i] == "I" else (r:=r-1) for i in range(len(s))] + [l+1] if r else t.diStringMatch(s, r=len(s)+1)
    
    '''
      Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
      Solution: 
        Case r.val >= m: return 1 + s.goodNodes(r.left, r.val) + s.goodNodes(r.right, r.val)
        Case r.val <  m: return 0 + s.goodNodes(r.left, m)     + s.goodNodes(r.right, m)
      Complexity: Time O(n) (one recusive call to each node)
    '''
    goodNodes = lambda s, r, m = -10001: int(r.val>=m) + (s.goodNodes(r.left, max(m, r.val)) if r.left else 0) + (s.goodNodes(r.right, max(m, r.val)) if r.right else 0)
    
    '''
      Problem: https://leetcode.com/problems/largest-palindrome-product/
      Solution: Preprocesses all possible solutions
      Complexity: Time O(1) Space O(1)
    '''
    largestPalindrome = lambda s, n : [9, 987, 123, 597, 677, 1218, 877, 475][n-1]
    
    '''
      Problem: https://leetcode.com/problems/reverse-prefix-of-word/
      Solution: Reverse prefix containing c if c is in w
      Complexity: Time O(n)
    '''
    reversePrefix = lambda s, w, c : (w[:w.index(c)+1])[::-1] + w[w.index(c)+1:] if c in w else w
    
    '''
      Problem: https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
      Solution: if c is the target node return [c] else return [c] + all paths from adjacent to target
      Complexity: Time O(p*l) (where p is the number of paths, and l is the length of a path)
    '''
    allPathsSourceTarget = lambda s, g, c=0 : [[c]] if c == len(g)-1 else [[c] + p for a in g[c] for p in s.allPathsSourceTarget(g, a)]
    
    '''
      Problem: https://leetcode.com/problems/k-closest-points-to-origin/
      Solution: sort by euclidean distance between each point and origin (ignoring sqrt)
      Complexity: Time O(nlogn)
    '''
    kClosest = lambda _, p, k : sorted(p, key = lambda a: a[0] * a[0] + a[1] * a[1])[:k]

