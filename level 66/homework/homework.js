function sumOfArray(arr) {
    return arr.reduce((acc, curr) => acc + curr, 0);
}



function minMaxOfArray(arr) {
    return {
        min: Math.min(...arr),
        max: Math.max(...arr)
    };
}

function generateRandomArray(N) {
    return Array.from({ length: N }, () => Math.floor(Math.random() * 100) + 1);
}


function squareArray(arr) {
    return arr.map(x => x * x);
}


function roundNumber(num) {
    return {
        floor: Math.floor(num),
        ceil: Math.ceil(num),
        round: Math.round(num)
    };
}