import * as fs from 'fs';

const input = fs.readFileSync('/dev/stdin', 'utf8').split(' ');
const N = +input[0];
const K = +input[1];

let array = [...Array(N + 1)].map((_: undefined, idx: number) => idx);
console.log(array);
