function isPrime(n) {
    if (n<=1) return false;
    else if (n == 2) return true;
    let flag = true;
    for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
        if (n % i == 0) {
            flag = false;
            break;
        }
    }
    return flag;
}

function firstPrimes(m) {
    let count = 0;
    let prime_list = []
    let i = 1;

    while(count<m){
        if (isPrime(i)){
            count++;
            prime_list.push(i);
        }
        i++;
    }
    return prime_list;
}










// CODE RUNNING AND TESTING
const PRIME_ARRAY = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
/*
for (let i = 0; i < 50; i++) {
    let temp = Math.ceil(Math.random() * 100);
    let isPrimeResult = isPrime(temp);
    console.log(temp, isPrimeResult)
    console.log("verification", PRIME_ARRAY.includes(temp))
    console.log("--")
}
*/
console.log(isPrime(2))
console.log(firstPrimes(PRIME_ARRAY.length), PRIME_ARRAY)