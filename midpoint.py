 
function midRect(f:Function, a:Number, b:Number, n:uint):Number
{
	var sum:Number = 0;
	var dx:Number = (b-a)/n;
	for (var x:Number = a + (dx / 2); n > 0; n--, x += dx)
		sum += f(x);
	return sum * dx;
