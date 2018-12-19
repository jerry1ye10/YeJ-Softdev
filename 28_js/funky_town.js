//Team Octo-happiness: Clara, Jerry, and Jason
//SoftDev1 pd7
//K28 -- Sequential Progression
//2018-12-19
// recursive function for returning nth number in the fibonacci sequence
var fibonacci = (n) => {
    if (n < 2){
        return n;
    }
    return fibonacci (n-1) + fibonacci(n-2);
}

/ **************
 gcd returns the greatest common denominator for ints a, b
 This method uses Euclid's algorithm to find GCD recursively.                
 First, the larger and smaller inputs are identified.  
 If either is equal to 0, then 0 is returned. 
 If large is divisible by small, then small is returned      
 Otherwise, large becomes largest - small and the gcdER of these two integers
 is called.
*************** /
var gcd = (a, b) =>{
    var large = max(a, b);
    var small = min(a, b);
    if (small == 0){
        return 0;
    }
    if (large %small == 0){
        return small;}
    else {
            large = large - small;
        return gcd(large, small);
    }
}

// helper function return max of a and b
var max = (a, b) => {
    if (a > b){
	return a;
    }
    return b;
}

// helper function returns min of a and b
var min = (a, b) => {
    if (a < b){
	return a;
    }
    return b;
}


// function for returning random 
var randomStudent = () =>{
    var students = ['jerry','clara','jason'];
    var index = Math.floor((Math.random() * students.length));
    return students[index];
}
