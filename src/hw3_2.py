def palindrome(txt):
  lowercase=txt.lower()
  split=lowercase.split()

  new_list=[]
  for i in split:

    i=i.replace(".","")
    i=i.replace(",","")
    new_list.append(i)

  my_sting="".join(new_list)

  if my_sting[::]==my_sting[::-1]:
    return True

  else:
    return False