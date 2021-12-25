def count7(n):
    #base case
    if n==0:
        return 0
    if n%10 == 7:
        return 1 + count7(n//10)
    else:
        return 0 + count7(n//10)

# //regular count7
# Int count = 0;
# While (n!=0){
# If (n%10 ==7)
#    count+;
# n = n/10;
#
# Return count;
