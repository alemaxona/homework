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

// 2
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

// 3
// ?? Доделать!
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

// 4
var value1 = +prompt('Number1', '');
var value2 = +prompt('Number2', '');
while(value1 != value2) {
    if (value2 == 0) {
        alert('Value2 = 0') 
        break; 
    } else if (value1 == 0) { 
        value1++;
        continue;
     }else {
         if (value1 % 5 == 0) {
             console.log('Number is', value1, 'multiple of 5')
             value1++;
             continue;
         }
     } 
     value1++;
}

// 5
// Создать лист из 6 любых чисел. Отсортировать его по возрастанию
var value1 = [5, 2, 4, 3, 1];
value1.sort() ; // reverse() - в обратном порядке
console.log(value1);

// 6
// Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
var dict = {1:'a', 2: 'b', 4:'c', 3:'3'}
for (i in dict) {
    console.log(i, ':', dict[i]);
}

// 7 
// ??? tuple
// Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
// var tuple = (1.23, 23.5, 13.6, 234.5567, 5.678, 0.456467, 0.56778, 9.234, 100.4545, 379.32435);

// 8
// Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
var list = ['Earth', 'Russia', 'Moscow'];
console.log(list[0],'->', list[1], '->', list[2]);

// 9
// Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
var str = '/bin:/usr/bin:/usr/local/bin';
var list = str.split(':');
console.log(list);

// 10
// Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
var min = 1;
var max = 100;
while(min != max) {
    if (min % 7 == 0) { console.log (min, 'Yes'); min++ } else { console.log(min, 'No'); min++; }  
}

// 11
