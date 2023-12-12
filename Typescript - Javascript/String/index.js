//count vowels
function countVowel(inputString){
    let count = 0;
    const VOWEL = 'aeiou';
    let stringArray = inputString.toLowerCase().split("");
    for(let i = 0; i < stringArray.length; i++){
        if(VOWEL.includes(stringArray[i])){
            count++;
        }
    }   
    return count;
}
console.log(countVowel('heeloloo'))

//reverse string
function reverseString(inputString){
    return inputString.split("").reverse().join("");
}

console.log(reverseString("iamsohel"));

//reverse sentence's word
function reverseString(inputString){
    return inputString.split(" ").reverse().join(" ");
}
console.log(reverseString("Trees are beautiful"))


function duplicateStringRemove(str){
    let arrayOfString = str.split("");
    let uniqueArrayOfString = [];
    arrayOfString.forEach(char => {
        if(!uniqueArrayOfString.includes(char)){
            uniqueArrayOfString.push(char);
        }
    })

    return uniqueArrayOfString.join("")
}
console.log(duplicateStringRemove("helllooo!!"));

function findMostRepeatedCharacter(str){
    let arrayOfString = str.split("");
    let obj = {};
    arrayOfString.forEach(char => {
        if(obj.hasOwnProperty(char)){
            obj[char] += 1;
        } else {
            obj[char] = 1;
        }
    });
    let bigger = -1;
    let mostFre;
    for(let elem in obj){
        if(obj[elem] > bigger){
            bigger = obj[elem];
            mostFre = elem;
        }
    }

    console.log(mostFre)
}

findMostRepeatedCharacter('gkjgjgjhjh');

function capitalEachWord(sentences){
    let words = sentences.split(" ");
    let sen = words.map(word => {
        return word.charAt(0).toUpperCase() + word.slice(1).trim();
    })

    return sen.join(" ")
}

console.log(capitalEachWord(' trees are   beautiful '))

function checkAnagram(str1, str2){
    let num1 = 0;
    let num2 = 0;
    for(let n1 in str1){
        num1 += str1.charCodeAt(n1);
    }

    for(let n2 in str2){
        num2 += str2.charCodeAt(n2);
    }
    
    if(num1 == num2){
        return true;
    } else {
        return false;
    }
}

console.log(checkAnagram('abcd', 'bcda'))
//console.log(checkAnagram('abcd', 'bcde'))

function checkPalindrome(str){
   let reverseString = str.split("").reverse().join("");
   if(str === reverseString){
       return 'Palindrome'
   } else {
       return 'Not Palindrome'
   }
}

console.log(checkPalindrome('dad'))
console.log(checkPalindrome('das'))