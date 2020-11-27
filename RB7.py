a=input('introduceti CNP: ')
n=0
if (len(a)<13)or(len(a)>13):
    print('CNP este fals')
else:
    for i in a:
        if ord(i) in range(48,58):
            n+=1
    if n==13:
        print('CNP este adevarat')
    else:
        print('CNP este fals')