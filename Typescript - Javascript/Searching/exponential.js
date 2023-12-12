function exponentialSearch(arrayOfNum, target){
    var bound = 1;
    while(bound < arrayOfNum.length && arrayOfNum[bound] < target) {
        bound = bound * 2;
    }

    var left = bound/2;
    var right = arrayOfNum.length - 1;
    return binarySearch(arrayOfNum, target, left, right)
    
}

function binarySearch(arrayOfNum, target, left, right) {
    
    if(left > right) {
        return -1;
    }
    var mid = Math.floor(left + right) / 2;
    if(arrayOfNum[mid] === target){
        return mid;
    }

    if(target < arrayOfNum[mid]) {
        return binarySearch(arrayOfNum, target, left, mid -1);
    } else {
        return binarySearch(arrayOfNum, target, mid + 1, right)
    }
}

let result = exponentialSearch([1,2,26], 1);
console.log(result)

