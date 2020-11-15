aa = "account[0].id"

a = "account[0]"

test_aa = aa.split('.')
for j, v in enumerate(test_aa):
    print(j,v)
    if v.find('[') > 0 :
        start = v.find('[')
        end = v.find(']')
        key = v[0 : start]
        index = v[(start+1): end]
        print('field is: %s,index is: %s' % (key,index))
    else:
        print(v)
        # print('filed is: %s' %v)

print(a.find('1'))
print(a.find('0'))
print(a[(a.find('[') + 1): a.find(']')])