class Solution {

    public static void dfs(int i, int j, int m, int n, char[][] grid){//originally had || grid[i][j] but you dont need it, as additionally and initial DFS are executed with the assumption that the place is a '1'
            if( i >= m || j >= n || i < 0 || j < 0){//oh my god i had j<= 0 which was causing all the multiple counts
                return;
            }
            else if(grid[i][j] == '1'){
                grid[i][j] = '0';
                dfs(i-1, j, m, n, grid);//checking down!
                dfs(i, j-1, m, n, grid);//checking left
                dfs(i+1, j, m, n, grid);//checking up
                dfs(i, j+1, m, n, grid);//checking right
            }
            else return;

        }




    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;//finding size of the inner array
        int count = 0;
        for(int i = 0;  i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    dfs(i, j, m, n, grid);//we want to depth first search and probably replace the 1's we have searched with something else, probably zero so they dont get additionally check at all 
                    count++;//dfs should all connected 1's from up, down, left and right
                }
                //since we are altering the graph, every time we find a new 1, we know it will be a new island, since we fully traverse the full island whenever we encounter a new 1 and destroy the grid behind our visited and connected components
            }
        }
        return count;
    }
}


/*
Final thoughts, 
This took me about 3 hours to formulate the strategy, and i originally wanted to take a union graph approach, but changed when I had the idea to mutate the matrix every time we find a 1, I used 1 hint from chatgpt that said the following
-----
Think of the grid as a graph where each '1' is a node, and adjacent '1's (up, down, left, right) form connected components. Your goal is to count these connected components. A useful approach is to visit each '1' and mark all the land in its connected component as visited before moving on. A common technique for this involves either Depth-First Search (DFS) or Breadth-First Search (BFS). Which one you choose depends on how you like to explore the grid!
-----
This ultimately wasnt that helpful as i knew it could be a depth first search problem
*/