def listCompare(src_lst,dst_lst):
    if 0 == len(src_lst) or 0 == len(dst_lst):
        print "empty list"
        exit()
    if len(src_lst) != len(dst_lst):
        print "list size different! no further comparison needed."
        exit()
    for item in src_lst:
        if item not in dst_lst:
            print "item : %s not in dst_lst! quit!" %item
            exit()



l1=[11,22,33,44,55]
l2=[11,22,33,44,55,66,77]
l3=[11,22,33,332,44]

print "------L1,L2-----------"
listCompare(l1,l3)
print "------L3,L2-----------"
#listCompare(l3,l2)
print "------L2,L1-----------"
listCompare(l2,l1)