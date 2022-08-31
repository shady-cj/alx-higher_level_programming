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
	printf("[*] Allocated = %d\n", (PyListObject *)p->allocated);

	for (index = 0; index < size; index++)
	{
		entry = PyList_GET_ITEM(p, index);
		if (PyBytes_Check(entry))
		{
			printf("Element %lu: bytes\n", index);
			print_python_bytes(p);
		}
		else
		{
			printf("Element %lu: %s", index, p->ob_type);
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
	size_t size;
	char *b_str;

	printf("[.] bytes object info\n");
	size = PyBytes_Size(p);
	printf("  size: %lu\n", size);
	b_str = PyBytes_AsString(p);
	printf("trying string: %s\n", b_str);
}
