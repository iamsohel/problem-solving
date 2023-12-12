function selectionSort(arrayOfNums) {
    for(let i = 0; i < arrayOfNums.length; i++) {
        var minIndex = i;
        for(let j = i; j < arrayOfNums.length; j++){
            if(arrayOfNums[j] < arrayOfNums[minIndex]) {
                minIndex = j;
            }
        }
        let temp = arrayOfNums[minIndex];
        arrayOfNums[minIndex] = arrayOfNums[i];
        arrayOfNums[i] = temp;
    }
    for(let i = 0; i < arrayOfNums.length; i++){
        console.log(arrayOfNums[i])
    }
}

selectionSort([1, 3, 2, 5, 4])