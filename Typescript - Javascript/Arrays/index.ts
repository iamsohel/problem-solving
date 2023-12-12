function findTwoSumIterative(arrays: number[], target: number): number[] {
    for(let i=0; i< arrays.length - 1; i++){
        for(let j=i+1; j< arrays.length; j++){
            if(arrays[i] + arrays[j] == target){
                return [i, j]
            }
        }
    }
    return [];
}

//1,3,5,7 = 8

// let result = findTwoSumIterative([-1,3,5,-7], 8);
// console.log(result)

function twoSumWithObject(arrays: number[], target: number): number[]{
    let arrayObject = {};
    for(let i=0; i < arrays.length; i++){
        let firstNumber = arrays[i];
        let secondNumber = target - firstNumber;
        console.log(secondNumber)
        if(arrayObject.hasOwnProperty(secondNumber)){
            return [arrayObject[secondNumber], i]
        }
        arrayObject[firstNumber] = i;
        console.log(arrayObject)
    }
    return []
}

 let result2 = twoSumWithObject([1,3,5,7], 10);
 console.log(result2)