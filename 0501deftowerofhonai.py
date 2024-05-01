def move(mfrom,temp,mto,n):
    if n == 1:
       print(f'move disc form {mfrom} to {mto}')
    else:
       move(mfrom,mto,temp,n-1)
       move(mfrom,temp,mto,1)
       move(temp,mfrom,mto,n-1)


move("A","B","C",3)