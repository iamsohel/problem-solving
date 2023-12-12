function bubbleSort(arrayOfNums){
    for (let i = 0; i < arrayOfNums.length; i++) {
        for(let j = 1; j< arrayOfNums.length - i; j++){
            if(arrayOfNums[j] < arrayOfNums[j - 1]){
                let temp = arrayOfNums[j];
                arrayOfNums[j] = arrayOfNums[j - 1];
                arrayOfNums[j-1] = temp;
            }
        }
    }
    for(let i = 0; i < arrayOfNums.length;  i++) {
        console.log(arrayOfNums[i])
    }
}

bubbleSort([2, 6, 3 , 5])