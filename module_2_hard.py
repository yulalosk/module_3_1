n=int(input('Введите число от 3 до 20 '))
result=''
for i in range(1,n):
     for j in range(2,n):
          if i < j:
               if n % (i+j)==0:
                    result=result+str(i)+str(j)
print(result)







