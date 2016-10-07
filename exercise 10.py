'''
def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for i in t:
        total += sum(i)
    return total


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    result = []
    total = 0
    for i in t:
        total += i
        result.append(total)
    return result
t = [1,2,3]
print(cumsum(t))

def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    n = len(t) - 1
    return t[1:n]

t = [1, 2, 3, 4]
print(middle(t))

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    n = len(t) - 1
    return t[1:n]

def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    c = t[0:]
    c.sort()
    if c == t:
        return True
    else:
        return False

print(is_sorted([1,2,3,5,4]))
 

def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    for i in word1:
        if word1.count(i) == word2.count(i):
            return True
        else:
            return False
print(is_anagram('different','letters'))

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    for i in s:
        if s.count(i) > 1:
            return True
    return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    i = 0
    while i < len(s):
        if s[i] == s[i+1]:
            return True
        else:
            i += 1
    return False
print(has_adjacent_duplicates('abbc'))


def binary_search(my_list, x):
    """
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    """
    b = my_list[0:]
    n = len(my_list)
    
    

    while n > 1:
        n = len(my_list)
        
        if abs(x-my_list[int(n/2)]) <= 0.001:
            return b.index(x)
            
        else:
            if x > my_list[int(n/2)]:
                my_list = my_list[int(n/2):]
               
    
            elif x < my_list[int(n/2)]:
                my_list = my_list[0:int(n/2)]
            
            
    return None
  

        


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
'''


low = 0
high = len(my_list) - 1
while low<=high:
    mid = int((low+high)/2)
    if x == my_list[mid]:
        return mid
    elif x < my_list[mid]: