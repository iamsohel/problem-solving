function binarySearchIterative(arrayOfNum, target){
    var left = 0;
    var right = arrayOfNum.length - 1;

    while(left <= right) {
        
        let mid = Math.floor(( left + right ) / 2);
        console.log(left, right, mid)
        if(arrayOfNum[mid] == target){
            return mid;
        }

        if (target < arrayOfNum[mid]){
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return -1;
}

function binarySearchRecursive(arrayOfNum, target, left, right){
   
    if(right < left) {
        return -1;
    }
    
    let mid = Math.floor((left + right) / 2);

    if(target === arrayOfNum[mid]){
        return mid;
    }
    if(target < arrayOfNum[mid]){
        return binarySearchRecursive(arrayOfNum, target, left,  mid - 1)
    } else {
        return binarySearchRecursive(arrayOfNum, target,  mid + 1, right)
    }
}

// let result = binarySearchIterative([1, 2, 3, 5], 1);
// console.log(result)

let result = binarySearchRecursive([1, 2, 3, 5], 5, 0, 3);
console.log(result)

//O(logn)