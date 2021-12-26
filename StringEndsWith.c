#include <stdbool.h>
#include <string.h>
bool solution(const char *string, const char *ending)
{
  int end_len=strlen(ending);
  if(end_len==0){
    return true;
  }
  int str_len=strlen(string);
  if(str_len==0&&end_len>0){
    return false;
  }
  int diff=str_len-end_len; int i; int y;
  if(end_len>str_len){
    y=end_len-str_len;
  } else {
    y=0;
  }
  for(i=diff;i<str_len;i++){
    if(string[i]!=ending[y++]){
      return false;
    }
  }
  return true;
}
