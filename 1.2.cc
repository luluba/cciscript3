//Implement a function void reverse(char* str) in c or c++ which reverse a null-terminated string
#include <stdio.h>
#include <string.h>
#include <iostream>
void reverse(char* str)
{
	char* origin = str;
	char* start = str;
	
	while (*str != '\0')
	{
		str++;	
	}

	str--;//set one back, the last is null byte
	char tmp;
	while (start < str)
	{
		tmp = *start;
		*start = *str;
		*str = tmp;
		start++;
		str--;
	}	

	std::cout << origin << std::endl;
}

int main()
{
	char str[] = "abcde";
	reverse(str);
	return 0;
}
