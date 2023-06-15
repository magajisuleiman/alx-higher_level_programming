#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *strings;
	long int sizes;
	long int j;
	long int limits;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sizes = ((PyVarObject *)(p))->ob_size;
	strings = ((PyBytesObject *)p)->ob_sval;

	printf("  sizes: %ld\n", sizes);
	printf("  trying strings: %s\n", strings);

	if (sizes >= 10)
		limits = 10;
	else
		limits = sizes + 1;

	printf("  first %ld bytes:", limits);

	j = 0;
	while (j < limits)
	{
		if (strings[j] >= 0)
			printf(" %02x", strings[j]);
		else
			printf(" %02x", 256 + strings[j]);
		j++;
	}

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int sizes, j;
	PyListObject *list;
	PyObject *obj;

	sizes = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizes);
	printf("[*] Allocated = %ld\n", list->allocated);

	j = 0;
	while (j < sizes)
	{
		obj = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		j++;
	}
}
