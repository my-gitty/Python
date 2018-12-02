// MFCLibrary1.cpp : 定义 DLL 的初始化例程。
//

#include "stdafx.h"
#include "MFCLibrary1.h"


#define EXPORT1 __declspec(dllexport)
#include <iostream>
#include <string>
using namespace std;

class TestDLL {
public:
	void hello();
};

void TestDLL::hello()
{
	cout << "hello world \n";
}

extern "C" {
	TestDLL td;
	EXPORT1 void hello()
	{
		td.hello();
	}
	EXPORT1 void Hello()
	{
		cout << "Hello World \n";
	}

	EXPORT1 void add(double a, double b)
	{
		
		cout << "\na + b = " << a + b
			 << endl;
	}

	EXPORT1 const char* cov(const char* a)
	{
		cout << "input: " << a << endl;
		return a;
	}


	EXPORT1 TestDLL* Hello_New()
	{
		return new TestDLL();
	}

	EXPORT1 void Hello_print(TestDLL* foo)
	{
		foo->hello();
	}
}
