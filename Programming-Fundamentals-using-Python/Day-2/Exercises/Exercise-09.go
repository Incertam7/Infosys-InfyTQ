//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var courseFee float32 = 25000;
    var marks float32 = 70;
    var extraFee float32 = 1500;
    var scholarship float32 = marks * 0.5 * courseFee / 100;
    finalFee = courseFee - scholarship + extraFee;

     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
