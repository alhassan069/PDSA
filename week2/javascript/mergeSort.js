function merge(A, B) {
    let [m, n] = [A.length, B.length];
    let [C, i, j, k] = [[], 0, 0, 0];

    while (k < m + n) {
        if (i == m) { // A is empty
            C.push(...B.slice(j)); // push remaining of items from B to C
            k = k + (n - j); 
        } else if (j == n) {
            C.push(...A.slice(i));
            k = k + (m - i);
        } else if (A[i] < B[j]) {
            C.push(A[i]);
            i++;
            k++;
        } else {
            C.push(B[j]);
            j++;
            k++;
        }
    }

    return C;
}


function mergeSort(arr){
    let n = arr.length;
    if(n<=1) return arr;

    let mid = Math.floor(n/2);

    let left = mergeSort(arr.slice(0,mid));
    let right = mergeSort(arr.slice(mid));

    let merged = merge(left,right);

    return merged;
}



(function main(){
    let unsorted_arr = [1,0,0,0,-66,3,654,33,4,2,62,754,51,0,9];
    console.log(mergeSort(unsorted_arr));
}())