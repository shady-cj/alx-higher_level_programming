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

	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %ld", ((PyListObject *)p)->allocated);
	for (index = 0; index < size; index++)
	{
		el = PyList_GetItem(p, index);
		printf("Element %d: %d", index, Py_TYPE(el));
	}
}
