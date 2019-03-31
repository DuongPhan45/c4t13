n= int (input ("Tinh tong day so tu 1 den "))
# sum= n*(n+1)/2
sum= 0
for a in range (1, n+1):
    sum += a
print ("Tong cac so tu 1 den", n," la ", sum)
# a=a+b co the viet la a+=b