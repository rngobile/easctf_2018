
# This file was *autogenerated* from the file ciphertext_to_plain.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120 = Integer(7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120)# Need to find padding for this to work.
c = _sage_const_7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120 

'''
for x in range(0,len(str(c)), 8):
    print x
    print "chomp: " + str(c)[x:x+8]
'''

text = ''.join([unichr(int(str(c)[i:i+_sage_const_3 ])) for i in range(_sage_const_0 ,len(str(c)), _sage_const_3 )])
print text

