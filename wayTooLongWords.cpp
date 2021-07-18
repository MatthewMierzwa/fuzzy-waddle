#include <bits/stdc++.h>
/* Way Too Long Words   https://codeforces.com/problemset/problem/71/A  --  Accepted*/
using namespace std;

int main() {
	int n;
	cin>>n;
	string a[n];
	string s;
	for(int i = 0; i < n; i++){
		cin>>a[i];
	}
	for(int i = 0; i < n; i++){
		s = a[i];
		int z = s.length();
		if(z<=10){
			cout<<s<<"\n";
		} else {
			cout<<s[0]<<s.substr(1,z-2).length()<<s[z-1]<<"\n";
		}
	}
}

