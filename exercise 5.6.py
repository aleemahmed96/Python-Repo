age=int(input('enter your age'))
if age>=0 and age<2:
    print ("this is a baby")
elif age>=2 and age<4:
    print ("this is a toddler")
elif age>=4 and age<13:
    print ("this is a kid")
elif age>=13 and age<20:
    print ("this is a teenager")
elif age>=20 and age<65:
    print ("this is an adult")
elif age>=65:
    print ("this is an elder")
else:
    print ('you have lost your mind!!!')
