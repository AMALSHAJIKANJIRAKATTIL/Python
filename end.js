let fs = require("fs");
let data = fs.readFileSync('end.txt', 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1].trim();
}


let x=readLine().split(" ").map(Number)
console.log(x)

//let end=x.length-1;
let temp=0;
for(let i=0;i<x.length;i++){
    if(x[i]===0){
        x.splice(i,1)
        x.push(0)
    }
}
console.log(x)