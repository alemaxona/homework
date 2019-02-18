'use strict'
// 1
var value1 = +prompt('Enter value1', '1');
var value2 = +prompt('Enter value2', '2');

if (value1 != 0 && value2 != 0) {
    var result = value1 + value2;
    console.log('Result -', result);
} else {
    alert('Value error')
}

//2
var value1 = +prompt('Enter value1', '1');
var value2 = +prompt('Enter value2', '2');
var value3 = prompt('Enter + or -', '+');
var result;
if (value1 != 0 && value2 != 0 && value3 == '+') {
    result = value1 + value2;
    console.log('Result -', result);
} else if (value1 != 0 && value2 != 0 && value3 == '-') {
    result = value1 - value2
} else { alert ('Value Error')}

//3
// var value1 = +prompt('Enter value1', '20');
var value1 = 20;
var simple = ''
// console.log('Simple', 2)
for (var i = 3; i <= value1; i++) {
    // console.log(i)
    for (var j = 2; j < i; j++) {
        if (i % j == 0) {
            console.log('Not Simple', i);
            break
        }
    }
}

