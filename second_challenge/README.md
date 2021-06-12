# Shift an Array

<!-- Description of the challenge -->

### Feature Tasks

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

<!-- Embedded whiteboard image -->

1. Problem Domain:

> > Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index

2. In/Out

> > Input: array, value <br>
> > Output: add value to array

3. Edge cases:

- Empty array
- Null
- Not an array

4. Visulization

> > Input: [2,4,6,-8], 5 <br>
> > Output: [2,4,5,6,-8]

> > Input: [42,8,15,23,42], 16 <br>
> > Output: [42,8,15,16,23,42]

5. Big-O: Look at the code below

6. Algortihm:

   1. Find the middle of the array
   2. If the index where lower than middle add value to first array else add to the second array.
   3. Add the value to the first array.
   4. Add the second array to the first array.

7. Pseudo Code

   1. Find the middle index.
   2. For i in range of array lentgh.
      1. If index lower than middle add arr1.
      2. If index higher than middle add to arr2
      3. add num to arr1
      4. add arr2 to arr1

8. Code

```python
def insertShiftArray(arr,num):# a has length of n
  if len(arr)%2 ==0:# If modules == 0
    middle = (len(arr)//2)# 1 time only
  else:# If modules != 0
    middle = (len(arr)//2)+1# 1 time only

  arr1=[]# 1 time only
  arr2=[]# 1 time only

  for i in range(len(arr)):# n/2 times
    if(i < middle) :
      arr1.append(arr[i])# 1 time in every loop
    else:
      arr2.append(arr[i])# 1 time in every loop


  arr1.append(num)# 1 time only
  for i in range (len(arr2)):# n/2 times
       arr1.append(arr2[i])# 1 time in every loop

  return arr1# 1 time only


```

> > Complexity = 1 + 1 + 1 + n/2 \* (1) + 1+ n/2 \* (1) +1

           = constants + n * (1)
           = constants + n* constant
           = n

> > Time Complexity =O(n) <br><br>

9. Verification:

In: [2,4,6,-8], 5
expected Out: [2,4,5,6,-8]

middle = len(arr)//2
for i in range(5):
i < 5 :
arr1=[2,4]
i > 5 :
arr2=[6,-8]

arr1=[2,4,5]
arr1=[2,4,5,6,-8]

return arr1

## Approach & Efficiency

<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

big_O is a Python module to estimate the time complexity of Python code from its execution time. It can be used to analyze how functions scale with inputs of increasing size. big_O executes a Python function for input of increasing size N , and measures its execution time.
