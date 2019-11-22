0096 Unique Binary Search Trees
```java
public int numTrees(int n) {
    // # of unique trees at length n
    int[] dp = new int[n + 1];
    
    // n = 0 is somehow 1 tree
    dp[0] = 1;
    
    // n = 1;
    dp[1] = 1;
    
    for (int length = 2; length <= n; length++) {
        for (int root = 1; root <= length; root++) {
            int left = dp[root - 1];
            int right = dp[length - root];
            dp[length] += left * right;
        }
    }
    return dp[n];
}
```  
    n = 0;     null   
    
    count[0] = 1
    
    
    n = 1;      1       
    
    count[1] = 1 
    
    
    n = 2;    1__       			 __2     
    		      \					/                 
    		     count[1]	   	count[1]	
    
    count[2] = 1 + 1 = 2
    
    
    
    n = 3;    1__				      __2__	                   __3
    		      \		            /       \			      /		
    		  count[2]		  count[1]    count[1]		count[2]
    
    count[3] = 2 + 1 + 2  = 5
    
    
    
    n = 4;    1__  					__2__					   ___3___                  
    		      \				 /        \					  /		  \			
    		  count[3]		 count[1]    count[2]		  count[2]   count[1]
    
                 __4				
               /
           count[3]   
    
    count[4] = 5 + 2 + 2 + 5 = 14     
