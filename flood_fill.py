class Solution(object):
         
        
    def floodFill(self, image, sr, sc, newColor):
        
        cc=image[sr][sc]
        h=len(image)
        w=len(image[0])
        
        def dfs(r,c):
            if(0<=r<h and 0<=c<w and image[r][c]==cc and image[r][c]!=newColor):
                image[r][c]=newColor
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        dfs(sr,sc)
        return image
        