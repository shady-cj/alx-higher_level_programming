#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Takes a python list and describes it.
 * @p: The PyObject of p.
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int size, index;
	PyObject *el;

	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (index = 0; index < size; index++)
	{
		el = PyList_GetItem(p, index);
		printf("Element %d: %s\n", index, Py_TYPE(el)->tp_name);
	}
}
