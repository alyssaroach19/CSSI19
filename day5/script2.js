/*
function f(x)
{
    return 3 * x + 7;
}
console.log(f(2));
console.log(f(12));
console.log(f(7));  


function g (x)
{
    return 5 * x + 5;
}
console.log(g(4));
console.log(g(10));
console.log(g(5));
console.log(g(3));

function h (x)
{
    return 5 *x ** 2 - 4 * x + 2;
}
console.log(g(4));
console.log(g(10));
console.log(g(5));
console.log(g(3));

function  i (x,y)
{
    return x ** 2 + y ** 2;
}
console.log(i(4,5));
console.log(i(5,7));
console.log(i(7,10));
*/

function j (x,y,z)
{
    return x + y + z;
}
console.log(j(4,5,6));
console.log(j(7,4,3));
console.log(j(10,6,2));

function k (r)
{
    return 2 * Math.PI * r;
}
console.log(k(10))
console.log(k(1))
console.log(k(1.5))

function l (a,b,c)
{
    var d = b**2 - 4 * a * c;

    if (d >= 0)
    {
        var srd = Math.sqrt(d);
        return (-1 * b + srd)/(2*a);
    }
    else
    {
        return NaN;
    
    }
}
console.log(l(1,4,4));
console.log(l(1,0,));