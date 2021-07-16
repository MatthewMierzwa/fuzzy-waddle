#include <iostream>

/* Watermelon problem solution :: https://codeforces.com/problemset/problem/4/A */

int main(int argc, char** argv) {
	
	int weight;
	std::cin>>weight;
	
	if(weight%2!=0){
		std::cout<<"NO";
	} else if (weight==2) {
		std::cout<<"NO";	
	} else {
		std::cout<<"YES";
	}
	
	return 0;
}
