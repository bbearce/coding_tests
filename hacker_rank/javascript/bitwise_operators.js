// Objective

// Today, we're practicing bitwise operations. Check the attached tutorial for more details.

// Task

// We define S to be a sequence of distinct sequential integers from 1 to n; in other words, S={1,2,3,...,n}. We want to know the maximum bitwise AND value of any two integers, a and b (where a<b), in sequence S that is also less than a given integer, k.

// Complete the function in the editor so that given n and k, it returns the maximum a & b < k.

// Note: The & symbol represents the bitwise AND operator.

// Input Format

// The first line contains an integer, q, denoting the number of function calls. 
// Each of the q subsequent lines defines a dataset for a function call in the form of two space-separated integers describing the respective values of n and k.

// Constraints
// 1<=q<=10^3
// 2<=n<=10^3
// 2<=k<=n
// Output Format

// Return the maximum possible value of a&b < k for any a<b in sequence S.

// Sample Input 0

// 3
// 5 2
// 8 5
// 2 2
// Sample Output 0

// 1
// 4
// 0
// Explanation 0

// We perform the following q=3 function calls:
// ...got to https://www.hackerrank.com/challenges/js10-bitwise/problem
// for pictures
// When n=5 and k=2, we have the following possible a and b values in set S={1,2,3,4,5}:

// The maximum of any  that is also  is , so we return .

// When  and , the maximum of any  in set  is  (see table above), so we return .
// When  and , the maximum of any  in set  is  (see table above), so we return .
// Sample Input 1

// 2
// 9 2
// 8 3
// Sample Output 1

// 1
// 2
// Explanation 1

// We perform the following  function calls:

// When  and , the maximum of any  in set  is  (see table above), so we return .
// When  and , the maximum of any  in set  is  (see table above), so we return .



function getMaxLessThanK(n, k){
    let max_anb = 0;
	for(var i=1;i<=n;i++){
        for(var j=i-1;j>0;j--){
            if((i & j) < k && (i & j) > max_anb){
                max_anb = (i & j);
            }
        }
    }

    return max_anb
}

