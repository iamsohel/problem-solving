function jumpSearch(arrayOfNum, target){

    var start  = 0;
    var blockSize = Math.floor(Math.sqrt(arrayOfNum.length));
    var next = blockSize;
    while(start < arrayOfNum.length && arrayOfNum[next-1] < target){
        start = next;
        next = next + blockSize;
        
        if(next > arrayOfNum.length) {
            next = arrayOfNum.length;
        }
    }
    for(let i = start; i < next; i++){
        if (arrayOfNum[i] === target){
            return i;
        }
    }
    return -1;
}

let result = jumpSearch([1, 4, 3, 5, 5], 5);
console.log(result)

//O(sqrt 0f n)