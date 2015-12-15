var found_numbers = {};
var myNum = 0;
var min = 1;
var max = 5;
var total = 0;

for(i=0; i<10000; i++) {
	myNum = Math.floor(Math.random()*(max-min+1))+min;
	if (myNum in found_numbers) {
		found_numbers[myNum]++;
	} else {
		found_numbers[myNum] = 1;
	}
}

for (var item in found_numbers) {
	console.log(item+":"+found_numbers[item]);
	total += found_numbers[item];
}
console.log ("total: "+total);
