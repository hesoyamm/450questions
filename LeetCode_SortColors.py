class Solution:
    def sort012(self,arr,n):
        # code here
        start = 0
        mid = 0
        end = len(arr)-1
    
        while(mid<=end):
            if(arr[mid]==0):
                arr[mid],arr[start]=arr[start],arr[mid]
                start+=1
                mid+=1
            elif(arr[mid==1]):
                mid+=1
            elif(arr[mid]==2):
                arr[mid],arr[end]=arr[end],arr[mid]
                end=end-1
        return arr;

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
