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


if __name__ == "__main__":

    print(multi_bracket_validation('{}'))
    print(multi_bracket_validation('{}(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('(){}[[]]'))
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('(]('))
    print(multi_bracket_validation('{(})'))
