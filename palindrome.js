let fs = require("fs");
let data = fs.readFileSync('input.txt', 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1].trim();
}

// -------- Do NOT edit anything above this line ----------
// Use readLine() for taking input, it will read one line of from the input  and is stored in string format

let x=readLine().split("")
//console.log(x)
let bool=false;
let mid=Math.floor(x.length/2)
if(x.length===1){
    bool=true;
}
else{
for(let i=0;i<mid;i++){
    let a=x.pop();
    //console.log(a);
    if(x[i].toLowerCase()===a.toLocaleLowerCase()){
        bool=true;
    }else{
        bool=false;
        break;
    }
}
}
if(bool){
    console.log("YES")
}else{
    console.log("NO")
}