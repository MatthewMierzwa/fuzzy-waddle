#include <limits.h>
int find_even_index(const int *values, int length) {
  int i; int m=INT_MAX; int mi=0; int h=0;
  for(i=0;i<length;i++){
    int ii;int iii;
    int ctr=0;int ctr2=0;
    for(ii=0;ii<i;ii++){
      ctr+=values[ii];
    }
    for(iii=ii+1;iii<length;iii++){
      ctr2+=values[iii];
    }
    if(ctr==ctr2){h=1;if(m>ctr){m=ctr;mi=i;}}
  }
  if(h==1){return mi;}else{return -1;}
}
