#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: A PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf("%02x", str[i] & 0xff);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: A PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);

        printf("Element %zd: ", i);

        if (PyBytes_Check(element))
        {
            printf("bytes\n");
            print_python_bytes(element);
        }
        else if (PyLong_Check(element))
        {
            printf("int\n");
        }
        else if (PyFloat_Check(element))
        {
            printf("float\n");
        }
        else if (PyTuple_Check(element))
        {
            printf("tuple\n");
        }
        else if (PyList_Check(element))
        {
            printf("list\n");
        }
        else if (PyUnicode_Check(element))
        {
            printf("str\n");
        }
        else
        {
            printf("Unknown\n");
        }
    }
}
