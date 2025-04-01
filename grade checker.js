const grades =[91,66,77,84,66];
const search=66;

/* function searchGrade(grades,search){
    for(let i=0; i < grades.length; i++){
        if (grades[i]===search){
            console.log("The grade exists!");
            break;
        
        }
    }
}
searchGrade(grades, search); 
function displayHours(start,end){
    for(let i=start; i<=end;i++){
        console.log(i+":00");}
}
displayHours(1,24);

const fruits = ['a', 'b', 'c'];

function searchFruit(fruits, searchPhrase){
    const foundFruit = fruits.find(fruit => fruit === searchPhrase);
    if (foundFruit){
        console.log(searchPhrase+'is present');}
    else{console.log('no such is present in this realm');}
    }
    searchFruit(fruits, 'd');
function greeting(name){
    console.log("hey"+ name);}
greeting(gaius);*/

const testScores=[7,3,6,8,2];
const arr=testScores.filter(function(ant){
    return ant+2;
});
console.log(arr);