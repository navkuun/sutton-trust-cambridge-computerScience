# Divide and Conquer

### Finding a number within a sorted list can be performed using divide and conquer to reduce the amount of searching that needs to be performed (a binary search). How this can be used to determine whether a) 120 and b) 38 are in the following list? Show the actions step by step.

1. Firstly a pointer would be created to the middle of the array, right of array and left of array
2. Next the list would have to be sorted
3. Then you would check the pointer to the middle of the array and see if it's greater or smaller than your number n 
4. If it is greater then we would know that n is on the right side(as it's sorted)
5. Another pointer to the middle of the right side would then be created, and the same check of greater/lower would repeat
6. This operation would continue until the pointer to the left side == right side, as they would now be on the same element
7. If the value matches your value then it would be returned
8. Otherwide if it does not, n does not exist in the list. 

---

### Suppose that we are able to search a list of 700 million items using this algorithm. What is the maximum number of comparisons that must be performed before finding an item or concluding that it is not in the list?

As in binary search space is divided by 2 each time,
then the time complexity would be O(logn) base 2
So for 700 million items,
it would be log(700 million) base 2, 
which would be 29.38, or roughly 29 comparisons
