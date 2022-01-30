#include <stdio.h>
#include </usr/include/limits.h>

int saturating_add(int x,int y){
	int sum,pos,neg=0;
	sum=x+y;
	pos=!(x&INT_MIN) && !(y&INT_MIN) && (sum&INT_MIN);
	neg=(x&INT_MIN) && (y&INT_MIN) && !(sum&INT_MIN);
	pos&&(sum=INT_MAX); neg&&(sum=INT_MIN);
	return sum;
}

int main(int argc,char** argv){
	int x,y,z=0;
	x=3; y=22; z=saturating_add(x,y);
	printf("%d + %d = %d\n",x,y,z);
	x=INT_MAX; y=INT_MAX; z=saturating_add(x,y);
	printf("%d + %d = %d\n",x,y,z);
	x=-2147483648; y=-2147483648; z=saturating_add(x,y);
	printf("%d + %d = %d\n",x,y,z);
	
	return 1;
}
