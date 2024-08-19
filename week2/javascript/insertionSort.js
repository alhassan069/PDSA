function insertionSort(arr){
    let n = arr.length;
    if(n<=1) return arr;


    for(let i = 0;i<n;i++){

        let j = i;

        while((j>0) && (arr[j-1] > arr[j])){
            let temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j--;
        }
    }


    return arr;
}

(function main(){
    let unsorted_arr = [1,-66,3,654,33,4,2,62,754,51,0,9];
    console.log(insertionSort(unsorted_arr));
}())