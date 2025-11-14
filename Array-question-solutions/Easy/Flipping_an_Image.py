class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        def reverse(arr):
            s,e= 0,n-1
            while s<e:
                arr[s],arr[e] = arr[e],arr[s]
                s+=1
                e-=1

        for i in range(n):
            reverse(image[i])
        
        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j]=0
        return image
        