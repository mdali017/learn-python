
import sys;
# print(sys.getrefcount(24532))
# print(sys.getrefcount("hitesh"))
# print(sys.getrefcount("h"))
# print(sys.getrefcount(1))

a = 3;
a = "chaiaurcode"
a = 3.1416

a = 5;
b = 2;
# print(a)
# print(a + 2)


myListOne = [1, 2, 4];
myListTwo = myListOne;
myListOne = 'chai';
# print(myListTwo)
# myListOne[0] = 33;
# print(myListOne)

h1 = [1, 2, 3]
h1[0] = 55
h2 = h1[:];
# print(h2)

import copy;
h2 = copy.copy(h1);
# print(h2)

n = [1, 2, 3];
m = n;
print(m, n);
print(m == n);
print(m is n)