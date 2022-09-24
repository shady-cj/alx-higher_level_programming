#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - This function prints python strings
 * @p: The PyObject
 * Return: Void
 */


void print_python_string(PyObject *p)
{
	ssize_t size;
	char *str;

	printf("[.] string object info\n");
	size = ((*PyVarObject)(p))->ob_size;
	printf("%lu\n", size);
}
