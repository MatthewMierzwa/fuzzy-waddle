#include <stddef.h>
#include <stdio.h>
size_t countBits(unsigned value);

size_t countBits(unsigned value){
  size_t count=0;
  if(value==0){
    return 0;
  }
  while(value!=0){
    if(value%2==1){
      count++;
    }
    value=value>>1;
  }
  return count;
}
