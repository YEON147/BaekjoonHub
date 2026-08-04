const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let str = "";

rl.on('line', function (line) {
    str = line;
}).on('close',function(){
    console.log(str);
});