//PF-Exer-16

num1 = 5
num2 = 10

//Write your code here

lcm = num1

if (num1 > num2)
{
    lcm = num1
}
else
{
    lcm = num2
}

while(lcm > 0)
{
    if(lcm % num1 == 0 && lcm % num2 == 0)
    {
        break
    }
    else
    {
        lcm++
    }
}

console.log(lcm)
