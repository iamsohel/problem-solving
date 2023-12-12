function findLessRepeatedCharacter(sentence){
    var character = {};
    for(let char in sentence){
        if(character.hasOwnProperty(sentence[char])){
            character[char] += 1;
        } else {
            character[char] = 1;
        }
    }
    console.log(character)
}   

findLessRepeatedCharacter("a green apple")

