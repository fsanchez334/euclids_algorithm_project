def euclid(one, two):
  string = ""
  a = one
  b = two

  if b == 0:
    string += "GCD" + '(' + str(a) + ',' + str(b) + ')' + "=" + " " + str(a)
    print(string)
    return a
  else:
    string = "GCD" + '(' + str(a) + ',' + str(b) + ')' + "="
    print(string, end = " ")
    return euclid(b, a % b)

euclid(270, 192)
