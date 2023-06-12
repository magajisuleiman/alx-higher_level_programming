#include <Python.h>

/**
 * print_python_list_info - Function that prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sizes;
	int allocs;
	int j;
	PyObject *obj;

	sizes = Py_SIZE(p);
	allocs = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sizes);
	printf("[*] Allocated = %d\n", allocs);

	j = 0;
	while (i < size)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);

		j++;
	}
}
