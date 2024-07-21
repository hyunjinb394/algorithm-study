package Gold;

import java.io.*;
import java.util.*;

public class Backjun_23326 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        boolean[] isSight = new boolean[N];
        TreeSet<Integer> sights = new TreeSet<>();
        
        for (int i = 0; i < N; i++) {
            isSight[i] = st.nextToken().equals("1");
            if (isSight[i]) {
                sights.add(i);
            }
        }
        
        int pos = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            if (type == 1) {
                int i = Integer.parseInt(st.nextToken()) - 1;
                isSight[i] = !isSight[i];
                if (isSight[i]) {
                    sights.add(i);
                } else {
                    sights.remove(i);
                }
            } else if (type == 2) {
                int x = Integer.parseInt(st.nextToken());
                pos = (pos + x) % N;
            } else if (type == 3) {
                if (sights.isEmpty()) {
                    sb.append("-1\n");
                } else {
                    Integer nextSight = sights.ceiling(pos);
                    if (nextSight == null) {
                        nextSight = sights.first();
                        sb.append((N - pos + nextSight) % N + "\n");
                    } else {
                        sb.append((nextSight - pos + N) % N + "\n");
                    }
                }
            }
        }
        
        System.out.print(sb.toString());
    }
}

