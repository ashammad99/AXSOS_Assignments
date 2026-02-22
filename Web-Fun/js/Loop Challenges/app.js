
console.log("showing odd numbers");
for (var i = 1; i <= 20; i++) {
    if (i % 2 != 0) {
        console.log(i);
    }
}

console.log("decreasing multiple of 3");
for (var i = 100; i >= 0; i--) {
    if (i % 3 == 0) {
        console.log(i)
    }
}


console.log("Print the given sequence ");
var array = [4, 2.5, 0.5, -2, -3.5];
for (var i = 0; i < array.length; i++) {
    console.log(array[i]);
}

console.log("Sigma");
var sum = 0;
for (var i = 1; i <= 100; i++) {
    sum += i;
}
console.log(sum);

console.log("Factorial");
var product = 1;
for (var i = 1; i <= 12; i++) {
    product *= i;
}
console.log(product);
