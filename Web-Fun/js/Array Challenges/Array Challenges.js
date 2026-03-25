console.log("1. Always Hungry\n");
function alwaysHungry(arr) {
    let result = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            result.push("yummy");
        }
    }

    return result.length ? result : "I'm hungry";
}

console.log(alwaysHungry([3.14, "food", "pie", true, "food"]));
// this should console log "yummy", "yummy"
console.log(alwaysHungry([4, 1, 5, 7, 2]));
// this should console log "I'm hungry"
console.log("-------------------------------------------");
console.log("2. High Pass Filter\n\n");
function highPass(arr, cutoff) {
    var filteredArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

console.log(highPass([6, 8, 3, 10, -2, 5, 9], 5)); // we expect back [6, 8y, 10, 9]
console.log("-------------------------------------------");
console.log("3. Better than average");
function betterThanAverage(arr) {
    var sum = 0;
    // calculate the average
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    let average = sum / arr.length;

    var count = 0
    // count how many values are greated than the average
    for (let j = 0; j < arr.length; j++) {
        if(arr[j] > average) {
            count++;
        }
    }
    return count;
}

console.log(betterThanAverage([6, 8, 3, 10, -2, 5, 9])); // we expect back 4
console.log("-------------------------------------------");
console.log("4. Array Reverse");
function reverse(arr) {
    let left = 0;
    let right = arr.length - 1;
//in place way, no need to new array
    while (left < right) {
        // Swap elements using a temporary variable
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        // Move pointers towards the middle
        left++;
        right--;
    }
    return arr;
}

console.log(reverse(["a", "b", "c", "d", "e"])); // we expect back ["e", "d", "c", "b", "a"]
console.log("-----------------------------------");
console.log("Fibonacci Array");
function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    if (n <= 0) return [];
    if (n === 1) return [0];
    var fibArr = [0, 1];
    // your code here //Iterative
    for (let i = 2; i < n; i++) {
        fibArr[i] = fibArr[i - 1] + fibArr[i - 2];
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]