const fs = require('fs');
const data = fs.readFileSync('./input_day1.txt').toString().split('\n').map(Number);
const testInput = [14, 1969, 100756];

// Part 1, with function expression
const fule_calculator1 = (mass) => Math.floor(mass / 3 - 2);
let part1_output = data.map((mass) => fule_calculator1(mass))
                       .reduce((acc, val) => acc + val);

console.log(part1_output);

// Part 2
function fule_calculator2(mass, sum=0){
    let fule = fule_calculator1(mass);
    if (fule > 0){
        sum += fule
        return fule_calculator2(fule, sum)
    };
    return sum
};
let part2_output = data.map((mass) => fule_calculator2(mass))
                       .reduce((acc, val) => acc + val);
console.log(part2_output)