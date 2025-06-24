// Last updated: 24/6/2025, 9:46:27 pm
public:
    int minValidStrings(vector<string>& v, string t) {
        int m = t.size();
        vector<int> dp(m);

        for(auto& w: v){
            int n = w.size();
            vector<int> p = prefix_function(w+'#'+t);
            for(int i=0; i<m; i++){
                dp[i] = max(dp[i], p[i+n+1]);
            }
        }

        m--;
        int a = 0;
        while(m>=0 and dp[m]>0){
            m-=dp[m];
            a++;
        }

        return m==-1 ? a: -1;
    }
};