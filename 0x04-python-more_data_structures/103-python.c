#include <Python.h>
#include <stdio.h>
void print_python_bytes(PyObject *p);
/**
 * print_python_list - This function takes in a Python list and
 * prints information about each entry in the list
 * @p: The python list of type PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	size_t size, index;
	PyObject *entry;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (index = 0; index < size; index++)
	{
		entry = PyList_GET_ITEM(p, index);
		if (PyBytes_Check(entry))
		{
			printf("Element %lu: bytes\n", index);
			print_python_bytes(entry);
		}
		else
		{
			printf("Element %lu: %s\n", index, (entry->ob_type)->tp_name);
		}
	}
}

/**
 * print_python_bytees - This function takes in a python byte and prints
 * information about the byte.
 * @p: The python byte of type PyObject
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	size_t size, max_byte, index;
	char *b_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %lu\n", size);
	b_str = PyBytes_AsString(p);
	printf("  trying string: %s\n", b_str);
	if ((size + 1) < 10)
	{
		max_byte = size + 1;
		printf("  First %lu bytes: ", max_byte);
	}
	else
	{
		max_byte = 10;
		printf("  First 10 bytes: ");
	}
	for (index = 0; index < max_byte; index++)
	{
		if (index + 1 == max_byte)
			printf("%x\n", b_str[index]);
		else
			printf("%x ", b_str[index]);
	}
}
