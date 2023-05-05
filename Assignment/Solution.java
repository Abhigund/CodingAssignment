import java.util.*;

class Solution {
    public static int makeAllConnected(int n, int[][] connections) {
        
        if (connections.length < n - 1) {
            return -1;
        }

        ArrayList<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] conn : connections) {
            int u = conn[0];
            int v = conn[1];
            graph[u].add(v);
            graph[v].add(u);
        }

        boolean[] visited = new boolean[n];
        int numComponents = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                numComponents++;
            }
        }

        return numComponents - 1;
    }

    static void dfs(int u, ArrayList<Integer>[] graph, boolean[] visited) {
        visited[u] = true;
        for (int v : graph[u]) {
            if (!visited[v]) {
                dfs(v, graph, visited);
            }
        }
    }


    public static void main(String[] args) {
        int n = 4;
        int[][] connections = {{0,1},{0,2},{1,2}};
        int ans = makeAllConnected(n, connections);
        System.out.println(ans);
    }
}
