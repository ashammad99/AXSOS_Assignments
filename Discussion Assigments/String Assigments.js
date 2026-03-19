//1. Reverse String
function reverseString(str) {
    let reveseStr = "";
    for (var i = str.length - 1; i >= 0; i--) {
        reveseStr += str[i];
    }
    return reveseStr;
}
console.log(reverseString("hello"));

//2- count Vowels - without using built in functions
function countVowles(str) {
    let count = 0;
    let x = str.toLowerCase();
    let vowelsArr = ["a", "e", "i", "o", "u"];
    for (var i = 0; i < vowelsArr.length; i++) {
        for (var j = 0; j < x.length; j++) {
            if (vowelsArr[i] == x[j]) {
                count++
            }
        }
    }
    return count;
}
console.log(countVowles("aeiou"));
console.log(countVowles("ahmed"));
//
function countVowles2(str) {
    let count = 0;
    let vowelsList = "aeiouAEIOU";
    for (var i = 0; i < str.length; i++ ) {
        if(str.includes(vowelsList)) {
            count++;
        }
    }
    return count;
}
console.log(countVowles2("aeiouAEIOU"));

//3. Check Palindrome without using built-in functions
function checkPalindrom(str) {
    return str == reverseString(str);
}
console.log(checkPalindrom("lool"));
console.log(checkPalindrom("ahmed"));

//3. Check Palindrome
function checkPalindrom2(str) {
    return str == str.split('').reverse().join('');
}
console.log(checkPalindrom2("lool"));
console.log(checkPalindrom2("ahmed"));
console.log(checkPalindrom2("madam"));

//4. Longest Word in a Sentence
function LongestWord(sentance) {
    let wordsArr = sentance.split(" ");
    let LongestWord = wordsArr[0];
    //Here Minimized the no of iteration by -1
    for (var i = 1; i < wordsArr.length; i++) {
        if (wordsArr[i].length > LongestWord.length) {
            LongestWord = wordsArr[i];
        }
    }
    return LongestWord;
}
console.log(LongestWord("I love solving algorithms"));


//Switch 
function convertLetter(character) {
    switch (character) {
        case "A":
            return "Excellent";
        case "B":
            return "Good job";
        case "C":
            return "You Passed";
        case "D":
            return "Need Improvement";
        case "E":
            return "Failed";
        default:
            return "Anything Else";
    }
}

console.log(convertLetter("A"));
console.log(convertLetter("G"));

//Count characters
function countCharacterTypes(str) {
    let countObject = { vowels: 0, digits: 0, spaces: 0, others: 0 };
    for (let i = 0; i < str.length; i++) {
        let char = str[i];

        switch (char) {
            case 'a': case 'e': case 'i': case 'o': case 'u':
            case 'A': case 'E': case 'I': case 'O': case 'U':
                countObject.vowels++;
                break;
            case '0': case '1': case '2': case '3': case '4':
            case '5': case '6': case '7': case '8': case '9':
                countObject.digits++;
                break;
            case ' ':
                countObject.spaces++;
                break;
            default:
                countObject.others++;
        }
    }

    return countObject;
}

console.log(countCharacterTypes("ahmed in 12 AA !!"));