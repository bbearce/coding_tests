// Objective

// In this challenge, we practice using JavaScript Template Literals. Check the attached tutorial for more details.

// Task

// The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named sides. Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the template's respective expression values.

// Complete the function in the editor so that it does the following:

// Finds the initial values of s1 and s2 by plugging the area and perimeter values into the formula:
// s = (P + sqrt(P^2-16*A))/4
// where A is the rectangle's area and P is its perimeter.
// Creates an array consisting of s1 and s2 and sorts it in ascending order.
// Returns the sorted array.
// Input Format

// The first line contains an integer denoting s1. 
// The second line contains an integer denoting s2.

// Constraints
// 1<=s1,s2<=100
// Output Format

// Return an array consisting of s1 and s2, sorted in ascending order.

// Sample Input 0

// 10
// 14
// Sample Output 0

// 10
// 14
// Explanation 0

// The locked code in the editor passes the following arrays to the tag function:

// The value of literals is [ 'The area is: ', '.\nThe perimeter is: ', '.' ].
// The value of expressions is [ 140, 48 ], where the first value denotes the rectangle's area, A, and the second value denotes its perimeter, P.
// When we plug those values into our formula, we get the following:

// s1 = 14
// s2 = 10
// We then store these values in an array, [14, 10], sort the array, and return the sorted array, [10, 14], as our answer.


function sides(literals, ...expressions) {
    const A = expressions[0]
    const P = expressions[1]

    const s1 = ( P + Math.sqrt(P**2 - 16*A) )/4
    const s2 = ( P - Math.sqrt(P**2 - 16*A) )/4
    
    var sides = [s1,s2].sort()
    return sides
}

s1 = 10
s2 = 14
const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;