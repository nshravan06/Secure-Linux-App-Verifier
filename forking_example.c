#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 
int main() 
{ 

	// make two process which run same 
	// program after this instruction
	int a[2]={2,3};
       printf("%d %d %d\n",a[0],a[1],a[2]);	
	fork(); 

	printf("Hello world!\n"); 
	return 0; 
} 

