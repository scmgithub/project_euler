// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, 
//  we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

var multiple_sum = 0;
var limit = 1000;
var div1 = 3;
var div2 = 5;

for (var i = 1; i<limit; i++) {
	if (i%div1===0 || i%div2===0) {
		multiple_sum+=i;
	}
}

console.log("The sum of all the multiples of "+div1+" and "+div2+" below "+limit+" is "+multiple_sum+".");
