"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x==0:
      return 0
    elif x==1:
      return 1
    else: 
      return foo(x-1)+foo(x-2)
    pass

def longest_run(mylist, key):
    result=0    # record longest run
    current=0   # record current length of run 
    for num in mylist:
      if num==key:
        current+=1 
      else:
        result=max(result,current)
        current=0
    return max(result,current)
    pass

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))    
    
def longest_run_recursive(mylist, key):
    # Base case: when list is empty or has only one element
    if len(mylist) < 2:
        if mylist and mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    # Recursive case: split mylist into two half and compute result for left and right lists
    left_list = mylist[:len(mylist) // 2]
    right_list = mylist[len(mylist) // 2:]
    left = longest_run_recursive(left_list, key)
    right = longest_run_recursive(right_list, key)
    # print(left_list,right_list)
    
    # Test if merged list is entire range
    if left.is_entire_range and right.is_entire_range:
        is_entire_range = True
    else:
        is_entire_range = False

    # left and right sizes are leftmost and rightmost run of input,
    # e.x. ([0,1,1,0,1,1,1,1],1) left size is 0 and right size is 4
    left_size = right.left_size + left.right_size if left.is_entire_range and left_list[-1] == key and right_list[0] == key else left.left_size
    right_size = right.left_size + left.right_size if right.is_entire_range and left_list[-1] == key and right_list[0] == key else right.right_size

    # if last element of left and the first of right and key are all equal,
    # then, two list are connected
    # a) two list are connected, the longest size would have four cases:
    # 1. in the middle, add up right size of left and left size of right
    # 2. longest in the left half,
    # 3. longest in the right half
    # 4. if one of lists or both is entire range, we need to add the size of that list to get the longest size.
    # b) two list are not connected, we ignore the case 1 and 4
    if left_list[-1] == key and right_list[0] == key:
        longest_size = max(left.right_size + right.left_size, left.longest_size, right.longest_size)
        if left.is_entire_range:
            longest_size = left_size + right.left_size
        if right.is_entire_range:
            longest_size = right_size + left.right_size
        if left.is_entire_range and right.is_entire_range:
            longest_size=left_size
    else:
        longest_size = max(left.longest_size, right.longest_size)

    # print(Result(left_size, right_size, longest_size, is_entire_range))
    return Result(left_size, right_size, longest_size, is_entire_range)
    pass


# Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

# print(longest_run_recursive([1,1,12,8,1,12,1,1,1,0,12,1], 1))
