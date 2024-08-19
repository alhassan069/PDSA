function selectionSort(arr){
    let n = arr.length;
    if(n <= 1){
        return arr;
    }
    for(let i = 0;i<n;i++){
        let minimum_position = i;
        for(let j = i+1;j<n;j++){
            if(arr[j]<arr[minimum_position]){
                minimum_position = j;
            }
        }
        let temp = arr[i];
        arr[i] = arr[minimum_position];
        arr[minimum_position] = temp;
    }

    return arr;
}

(function main(){
    let unsorted_arr = [1,-66,3,654,33,4,2,62,754,51,0,9];
    console.log(selectionSort(unsorted_arr));
}())