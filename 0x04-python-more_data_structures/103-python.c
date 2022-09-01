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
	int size, index;
	PyObject *entry;

	printf("[*] Python list info\n");
	size = ((PyVarObject*)(p))->ob_size;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (index = 0; index < size; index++)
	{
		entry = ((PyListObject *)p)->ob_item[index];
		printf("Element %d: %s\n", index, (entry->ob_type)->tp_name);
		if (PyBytes_Check(entry))
			print_python_bytes(entry);
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
	int size, max_byte, index;
	char *b_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject*)(p))->ob_size;
	printf("  size: %d\n", size);
	b_str = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", b_str);
	if ((size + 1) < 10)
	{
		max_byte = size + 1;
		printf("  First %d bytes: ", max_byte);
	}
	else
	{
		max_byte = 10;
		printf("  First 10 bytes: ");
	}
	for (index = 0; index < max_byte; index++)
	{
		if (index + 1 == max_byte)
			printf("%02hhx\n", b_str[index]);
		else
			printf("%02hhx ", b_str[index]);
	}
}
