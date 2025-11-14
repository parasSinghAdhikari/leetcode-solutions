# time complexity O(n*m*4)
# space complexity O(4+4) =O(1)
class Solution:
    def imageSmoother(self, img):
        temp = [-1,1,-1,1]
        diagonal = [(-1,-1),(1,1),(-1,1),(1,-1)]
        n = len(img)
        m = len(img[0])
        ans = [[0 for _ in range(m)]for _ in range(n)]

        for i in range(n):
            for j in range(m):
                sums = img[i][j]
                cnt =1
                for k in range(4):
                    l,r,ld,rd=i,j,i,j
                    if k<2:
                        l+=temp[k]
                    else:
                        r+=temp[k]
                    ld += diagonal[k][0]
                    rd += diagonal[k][1]
                    if (l>=0 and l<n) and (r>=0 and r<m):
                        cnt+=1
                        sums+=img[l][r]
                    if (ld>=0 and ld<n) and (rd>=0 and rd<m):
                        cnt+=1
                        sums+=img[ld][rd]
                ans[i][j]=sums//cnt
        return ans