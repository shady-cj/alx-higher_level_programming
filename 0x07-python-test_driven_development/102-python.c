#include "Python.h"
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
	size = ((PyASCIIObject *)(p))->length;
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %lu\n", size);
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
