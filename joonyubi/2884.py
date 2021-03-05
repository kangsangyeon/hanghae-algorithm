a, b = input().split()

a=int(a)
b=int(b)

b -= 45
if b<0:
    b+=60
    a-=1
    if a<0:
        a+=24

print(a,b)

'''
if (b-45<0): #분단위 조정이로 시 단위에 영향을 줄 경우
    if (a<1): #시단위 조정에서 음수가 될 경우
        a+=24
        
        b+=60
        
        print(a b)
    else: #시단위 조정이 필요 없는 경우
        b+=60
else: 

a-=1
b-=15
print(a b)
'''