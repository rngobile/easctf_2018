# Need to find padding for this to work.
c = 7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120

'''
for x in range(0,len(str(c)), 8):
    print x
    print "chomp: " + str(c)[x:x+8]
'''

text = ''.join([unichr(int(str(c)[i:i+3])) for i in range(0,len(str(c)), 3)])
print text

