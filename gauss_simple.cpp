#include <iostream>
#include <fstream>

using namespace std;

int n;

void solve(double**, double*, double*);

int main()
{
	ifstream f_in;
    f_in.open("data");

	f_in >> n;

	double **c = new double*[n];
    for (int i = 0; i < n; i++)
          c[i] = new double[n];

    double *x = new double [n];
    double *y = new double [n];
    double *a = new double [n];

	for (int i = 0; i < n; i++)
	{
        for (int j = 0; j < n; j++)
            f_in >> c[i][j];
		f_in >> y[i];
	};
	for (int i = 0; i < n; i++)
	{
        for (int j = 0; j < n; j++)
            cout << c[i][j] << " ";
	};

	//solve(c, y, a);

	for (int i = 0; i < n; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;

	f_in.close();

	cin.get();
	cin.get();
}

void solve(double** c, double* b, double* a)
{
    double d = 0;

    for (int j = 0; j < n - 1; j++)
        for (int i = j + 1; i < n; i++)
        {
            d = c[i][j] / c[j][j];

            for (int k = j; k < n; k++)
                  c[i][k] = c[i][k] - d * c[j][k];

			b[i] = b[i] - (d * b[j]);
        }
    
    a[n - 1] = b[n - 1] / c[n - 1][n - 1];

    for (int i = n - 2; i >= 0; i--)
    {
        d = b[i];
        for (int j = n - 1; j > i; j--)
            d -= c[i][j] * a[j];
        a[i] =  d / c[i][i];
    }
}
