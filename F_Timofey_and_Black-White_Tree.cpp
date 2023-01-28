#include <bits/stdc++.h>
using namespace std;

/* clang-format off */

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* FUNCTIONS */
#define f(i,s,e) for(long long int i=s;i<e;i++)
#define cf(i,s,e) for(long long int i=s;i<=e;i++)
#define rf(i,e,s) for(long long int i=e-1;i>=s;i--)
#define pb push_back
#define eb emplace_back

/* PRINTS */
template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; }

/* UTILS */
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define read(type) readInt<type>()
ll min(ll a,int b) { if (a<b) return a; return b; }
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }
void yes() { cout<<"YES\n"; }
void no() { cout<<"NO\n"; }

/*  All Required define Pre-Processors and typedef Constants */
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

template <class Head, class... Tail>
void print(Head&& head, Tail&&... tail){
  cout<<head<<' ';
  print(forward<Tail>(tail)...);
}

/* clang-format on */
vector<vector<int>> graph;
vector<int> arr;
vector<int> poss;
int curr = 1000000;

void bfs(int uu, int pp, int dd)
{
    vector<pair<int, pair<int, int>>> Q;
    Q.pb({dd, {uu, pp}});
    while(Q.size()>0)
    {
        int d = Q.back().first;
        int u = Q.back().second.first;
        int p = Q.back().second.second;
        Q.pop_back();
        poss[u] = d;
        
        for(int v:graph[u]){
            if(v!=p && poss[v]>(d+1) & (d+1)<curr){
                Q.pb({d+1, {v,u}});
            }
            
        }
    }
}

void solve()
{
    int n,c;
    cin>>n>>c;
    arr.assign(n , 0);
    curr = 1000000;
    poss.assign(n+2, 1000000);
    for(int i=0;i<(n-1);++i){
        cin>>arr[i];
    }
    
    graph.assign(n+1, vector<int>());
    for(int i=0;i<(n-1);++i){
        int a,b;
        cin>>a>>b;
        graph[a].pb(b);
        graph[b].pb(a);
    }
    
    bfs(c, 0, 0);
    
    
    
    for(int i=0;i<(n-1);++i){
        int u = arr[i];
        if(poss[u]<curr) { curr = poss[u];}
        cout<<curr<<" ";
        bfs(u,0,0);
    }
    cout<<"\n";
    
    
}

/* Main()  function */
int main()
{
    ios::sync_with_stdio(false);
	int tc;
	cin>>tc;

	while(tc--){
		solve();
	}
	
}
/* Main() Ends Here */