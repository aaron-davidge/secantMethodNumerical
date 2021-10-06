import math
# Python3 Program to find root of an
# equations using secant method
#CITED SOUCE https://www.geeksforgeeks.org/program-to-find-root-of-an-equations-using-secant-method/
#modified program with math function to use e and trig functions

# function takes value of x
# and returns f(x)
def f(x):
	
	# we are taking equation
	# as x^3+x-1
	f = math.exp(x) + 2**-x + 2*math.cos(x) - 6
	return f;

def secant(x1, x2, E):
	n = 0; xm = 0; x0 = 0; c = 0;
	if (f(x1) * f(x2) < 0):
		while True:
			
			# calculate the intermediate value
			x0 = ((x1 * f(x2) - x2 * f(x1)) /
							(f(x2) - f(x1)));

			# check if x0 is root of
			# equation or not
			c = f(x1) * f(x0);

			# update the value of interval
			x1 = x2;
			x2 = x0;

			# update number of iteration
			n += 1;

			# if x0 is the root of equation
			# then break the loop
			if (c == 0):
				break;
			xm = ((x1 * f(x2) - x2 * f(x1)) /
							(f(x2) - f(x1)));
			
			if(abs(xm - x0) < E):
				break;
		
		print("Root of the given equation =",
							round(x0, 6));
		print("No. of iterations = ", n);
		
	else:
		print("Can not find a root in ",
				"the given inteval");

# Driver code

# initializing the values
x1 = 1.3;
x2 = 2;
E = 0.00000001;
secant(x1, x2, E);

# This code is contributed by mits && Aaron Davidge
