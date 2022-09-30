#include <iostream>

long long factorial(int n){
  
  long int result = 1;
  
  if(n == 0 || n == 1){
    return result;
    
  }else{
    
    for(int i = 1; i <= n; ++i){
        result *= i;
    }
  }
  return result;
}

// Ternary operator
long long factorial(int n){
  return (n > 0) ? n * factorial(n - 1) : 1;
}