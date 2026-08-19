function solution(my_string, queries) {
    var ans = my_string.split('');
    for (i=0; i < queries.length; i++){
         let [s, e]  = queries[i];
         ans.splice(s, e-s+1,
                   ...ans.slice(s, e+1).reverse());
    }
    return ans.join('');
}