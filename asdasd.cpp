/*input
38
12
*/
#include <iostream>

using namespace std;


int main()
{
	int a,b,r;
	cin>>a>>b>>r;
	while (a % b != 0){
		r = a % b;
		a = b;
		b = r;
	}
	cout<<"Greatest Common Divisor is "<<r;
	return 0;
}