// hw from book
// 1
var value = '#'
for(i=0; i<7; i++) {
    console.log(value);
    value+='#'
}

// 2
var i = 1;
while (i < 101) {
    if ((i % 3 == 0) && (i % 5 == 0)) {
        console.log(i, 'FizzBuzz')
    } else if (i % 3 == 0) {
        console.log( i, 'Fizz')
    } else if (i % 5 == 0) {
        console.log(i, 'Buzz')
    }
    i++
}

// 3
var value = 64; a = '#'; i = 1; str = '';
while (i < value + 1) {
    if (i % 8 == 0) {
        str+=a
        str+= '\n'
        i++
        continue
    }
    if (a == '#') {
        str+= a
        a = ' '
    } else {
        str+=a
        a = '#'
    }
    i++
}
console.log(str);
