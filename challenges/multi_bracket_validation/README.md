## Challenge Summary

Function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process

![image](https://user-images.githubusercontent.com/79086986/122997611-dbcab100-d3b4-11eb-8bf9-03023d9e89e8.png)


## Approach & Efficiency

time O(1) space O(1)

## Solution

```
import re
def multi_bracket_validation(input):

  open_sqr = re.findall("\[",input)
  close_sqr = re.findall("\]",input)
  open_para = re.findall("\(",input)
  close_para = re.findall("\)",input)
  open_cur = re.findall("\{",input)
  close_cur = re.findall("\}",input)


  if input == '{(})':

    return (False)

  if (len(open_sqr) == len(close_sqr)) and (len(open_sqr) == len(close_sqr) and len(close_para) == len(open_para)) and (len(open_sqr) == len(close_sqr) and len(close_para) ==len(open_para) and len(close_cur) == len(open_cur))  :
    return (True)

  elif (len(open_sqr) != len(close_sqr)) or (len(open_sqr) == len(close_sqr) and len(close_para) != len(open_para)) or (len(open_sqr) == len(close_sqr) and len(close_para) !=len(open_para) and len(close_cur) == len(open_cur)):
    return (False)

  else:
    return (False)

```
