//PF-Exer-12
//This verification is based on string match.

package main
func main(){
    //Write your program logic here
    var num1 int = 3;
    var num2 int = 4;
    var num3 int = 1;
    
    var max int = 0;
    
    if(num1 > num2){
        if(num1 > num3){
            max = num1;
        }else{
            max = num3;
        }
    }else if(num2 > num3){
        max = num2;
    }else{
        max = num3;
    }
    println(max);
}
