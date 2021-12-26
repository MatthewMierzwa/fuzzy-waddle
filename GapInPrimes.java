import java.util.Arrays;

class GapInPrimes {
    
    public static long[] gap(int g, long m, long n) {
        long[] ret = {0,0};
        for(long e=m;e<n;e++){
          if(!is_prime(e)){ continue; }
          for(long r=1;r<=g;r++){
            if(r==g){
              if(is_prime(e+r)){
                ret[0]=e; ret[1]=e+r; return ret;
              }
            } else {
              if(is_prime(e+r)){
                e=e+r-1;
                break;
              }
            }
          }
        }
        return null;
    }
  
    public static boolean is_prime(long q){
      for(long i=2;i<q/2;i++){
        if(q%i==0){ return false; }
      }
      return true;
    }
}
