
# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_41 = Integer(41); _sage_const_175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671 = Integer(175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671); _sage_const_7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120 = Integer(7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120); _sage_const_5161910578063 = Integer(5161910578063); _sage_const_9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469 = Integer(9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469); _sage_const_67623079903 = Integer(67623079903); _sage_const_11 = Integer(11); _sage_const_1 = Integer(1)
n = _sage_const_9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469 
e1 = _sage_const_11 
e2 = _sage_const_41 
e3 = _sage_const_67623079903 
e4 = _sage_const_5161910578063 
e5 = _sage_const_175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671 
c = _sage_const_7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120 

e = e1 * e2 * e3 * e4 * e5

lst = continued_fraction(e/n)
conv = lst.convergents()
for i in conv:
	k = i.numerator()
	d = i.denominator()

	try:
		m = hex(int(pow(c,d,n)))[_sage_const_2 :-_sage_const_1 ].decode("hex")
		if "easyctf" in m:
			print m
	except:
		continue

