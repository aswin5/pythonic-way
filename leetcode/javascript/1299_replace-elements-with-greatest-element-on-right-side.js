/**
 * Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
 */



var test = function(arr){
    var viva = []
    for(var i =0; i<arr.length -2; i++){
        viva.push(Math.max(...arr.slice(i+1)));
    }
    viva.push(-1)
    return viva
}


var vida = [17,18,5,4,6,1]
var output = [18,6,6,6,1,-1]
// console.log(vida.splice(1))
console.log(test(vida))

