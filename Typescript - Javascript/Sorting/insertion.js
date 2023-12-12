function insertionSort(arrayOfNums){
    for(let i=0; i < arrayOfNums.length; i++){
        var current = arrayOfNums[i];
        var j = i-1;
        while(j >= 0 && arrayOfNums[j] > current){
            console.log(j)
            arrayOfNums[j + 1] = arrayOfNums[j];
            j--;
            console.log("j--",j)
        }
        arrayOfNums[j+1] = current;
    }
    for(let i=0; i < arrayOfNums.length; i++){
        //console.log(arrayOfNums[i])
    }
}

insertionSort([8, 5, 1 ,3])