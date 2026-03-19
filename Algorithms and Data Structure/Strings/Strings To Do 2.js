//1. Reverse String
function reverseString(str) {
    let reverseStr = "";
    for (var i = str.length - 1; i >= 0; i--) {
        reverseStr += str[i];
    }
    return reverseStr;
}
console.log(reverseString("Ahmed"));
console.log("=================================================");

//2. Remove Even-Length Strings
function removeEvenLengthStrings(arr) {
    let newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length % 2 !== 0) {
            newArr.push(arr[i]);
        }

    }
    return newArr;
}
let arr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."];
console.log(removeEvenLengthStrings(arr));
console.log("=================================================");
//3. Integer to Roman Numerals

console.log("=================================================");