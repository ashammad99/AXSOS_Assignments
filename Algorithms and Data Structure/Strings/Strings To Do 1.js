//1. Remove Blanks
function removeBlanks(str) {
    let newStr = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            newStr += str[i];
        }
    }
    return newStr
}
console.log(removeBlanks("Ahmed Salah Hammad"));
console.log("=================================================");

//2. Get Digits
function getDigits(str) {
    let newStr = "";
    for (var i = 0; i < str.length; i++) {
        if (!isNaN(Number(str[i])) && str[i] !== " ") {
            newStr += str[i];
        }
    }
    return newStr
}
console.log(getDigits("abc8c0d1ngd0j0!8 x 9"));
console.log("=================================================");

//3. Acronyms
function acronym(str) {
    let newArr = str.split(" ");
    let firstCharArr = [];
    for (var i = 0; i < newArr.length; i++) {
        firstCharArr.push(newArr[i][0])
    }
    result = firstCharArr.join("");
    return result.toUpperCase();
}
console.log(acronym("axsos learning managment system"));
console.log("=================================================");
//4. Count Non-Spaces
function countNonSpaces(str) {
    let count = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            count++;
        }
    }
    return count;
}
console.log(countNonSpaces("axsos learning managment system"));
console.log("=================================================");
//5. Remove Shorter Strings
function removeShorterStrings(arr, minLength) {
    let newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length >= minLength) {
            newArr.push(arr[i]);
        }
    }
    return newArr;
}
console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));