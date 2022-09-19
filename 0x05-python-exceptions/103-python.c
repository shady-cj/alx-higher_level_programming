#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - This function takes in a Python list and
 * prints information about each entry in the list
 * @p: The python list of type PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	ssize_t size, index;
	PyObject *entry;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject*)(p))->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	fflush(stdout);

	for (index = 0; index < size; index++)
	{
		entry = ((PyListObject *)p)->ob_item[index];
		printf("Element %ld: %s\n", index, (entry->ob_type)->tp_name);
		fflush(stdout);
		if (PyBytes_Check(entry))
			print_python_bytes(entry);
		else if (PyFloat_Check(entry))
			print_python_float(entry);
	}
}

/**
 * print_python_bytes - This function takes in a python byte and prints
 * information about the byte.
 * @p: The python byte of type PyObject
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	ssize_t size, max_byte, index;
	char *b_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject*)(p))->ob_size;
	printf("  size: %ld\n", size);
	b_str = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", b_str);
	if (size < 10)
		max_byte = size + 1;
	else
		max_byte = 10;
	printf("  first %ld bytes: ", max_byte);
	fflush(stdout);
	for (index = 0; index < max_byte; index++)
	{
		if (index + 1 == max_byte)
			printf("%02hhx\n", b_str[index]);
		else
			printf("%02hhx ", b_str[index]);
		fflush(stdout);
	}
}


/**
 * print_python_float - Prints info about python floating type
 * @p: The PyObject to check
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *buffer;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buffer = PyOS_double_to_string((((PyFloatObject *)(p))->ob_fval), 'r',
	       0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", buffer);
	fflush(stdout);
	PyMem_Free(buffer);
}
