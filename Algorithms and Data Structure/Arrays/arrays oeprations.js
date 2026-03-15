/*
console.log('1. Accessing Elements');
let colors = ["red", "blue", "green", "yellow", "purple"];
console.log(colors[0]);
console.log(colors[colors.length - 1]); 
console.log(colors[1]);
colors[2] = "orange"; 
console.log(colors); 
console.log("----------------------------------------");

console.log('2. Traversing an Array');
let numbers = [10, 20, 30, 40, 50];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]); 
}
for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}
console.log("------------------------------------------");

console.log('3. Searching in an Array');
let numbers2 = [5, 10, 15, 20, 25];
if (numbers2.indexOf(25) != -1) {
    console.log("Found at position " + numbers2.indexOf(25));
} else {
    console.log("Not Found");
}
console.log("------------------------------------------");

console.log('4. Sorting an Array');
let scores = [50, 20, 70, 10, 40];
scores.sort((a, b) => a - b);
console.log('Ascending Sorting: ' + scores);
scores.sort((a, b) => b - a); 
console.log('Descending Sorting: ' + scores);
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
console.log('sorting alphapitical order: ' + names.sort());
console.log("----------------------------------------------");

console.log('5. Inserting Elements');
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant"); 
console.log(animals);
animals.unshift("lion");
console.log(animals);
animals.splice(2, 0, "tiger");
console.log(animals);
console.log("------------------------------------------");

console.log('6. Deleting Elements');
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift(); 
console.log(fruits);
fruits.pop();
console.log(fruits);
fruits.splice(fruits.indexOf("banana"), 1);
console.log(fruits);
console.log("------------------------------------------");

console.log('7. Combining Arrays');
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
combinedArray = array1.concat(array2);
console.log(combinedArray);
console.log("------------------------------------------");

console.log('8. Splitting an Array');
let items = ["a", "b", "c", "d", "e"];
let firstArray = items.slice(0, 3);
let secondArray = items.slice(3, 5);
console.log(firstArray);
console.log(secondArray);
console.log("------------------------------------------------");

console.log('9. Filtering Elements');   
let number3  = [1, 5, 10, 15, 20, 25, 30];
let filteredArray = number3.filter((number) => number > 15);
console.log(filteredArray);
*/
console.log("----------------------------------------------------------------");
console.log('10. Advanced Challenge')
let duplicate = [1, 2, 2, 3, 4, 4, 5];
let unique = [];

for (let i = 0; i < duplicate.length; i++) {
    if (!unique.includes(duplicate[i])) {
        unique.push(duplicate[i]);
    }
}

console.log(unique);

let array = [1, 2, 3, 4, 5];
let n = 2;

for (let i = 0; i < n; i++) {
    let last = array.pop(); 
    array.unshift(last);   
}

console.log(array);
console.log("----------------------------------------------------------------");
/*
console.log('Bounes Challenge - Sorting Via Bubble Sorting Algorithm');
let input1 = [7, 10, 2];
let input2 = [1, 0, 3];
function sort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

sort(input1);
sort(input2);
for (var i = 0; i < input2.length; i++) {
  input1.push(input2[i]);
}
sort(input1);
console.log(input1);
*/