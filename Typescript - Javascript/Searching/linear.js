function linearSearch(arrayOfNum, target){
    for(let i = 0; i < arrayOfNum.length; i++){
        if (arrayOfNum[i] === target){
            return i;
        }
    }
    return -1;
}

let result = linearSearch([1, 4, 3, 5], 50);
console.log(result)

//O(n)