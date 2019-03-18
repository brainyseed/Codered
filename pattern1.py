#Print Pattern Input=N example N=3
#333222111
#332211
#321
def printPat(n):
    ori=n
    print_n=n
    ans=""
    while n>0:
        while print_n>0:
            for i in range(0,n):
                ans=ans+str(print_n)+" "
            print_n=print_n-1
        ans=ans+"$"
        #print("$", e)
        print_n=ori
        n=n-1
    return ans     
