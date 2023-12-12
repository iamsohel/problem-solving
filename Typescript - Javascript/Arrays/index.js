function findTwoSumIterative(arrays, target) {
    for (var i = 0; i < arrays.length - 1; i++) {
        for (var j = i + 1; j < arrays.length; j++) {
            if (arrays[i] + arrays[j] == target) {
                return [i, j];
            }
        }
    }
    return [];
}
//1,3,5,7 = 8
// let result = findTwoSumIterative([-1,3,5,-7], 8);
// console.log(result)
function twoSumWithObject(arrays, target) {
    var arrayObject = {};
    for (var i = 0; i < arrays.length; i++) {
        var firstNumber = arrays[i];
        var secondNumber = target - firstNumber;
        console.log(secondNumber);
        if (arrayObject.hasOwnProperty(secondNumber)) {
            return [arrayObject[secondNumber], i];
        }
        arrayObject[firstNumber] = i;
        console.log(arrayObject);
    }
    return [];
}
var result2 = twoSumWithObject([1, 3, 5, 7], 10);
console.log(result2);
