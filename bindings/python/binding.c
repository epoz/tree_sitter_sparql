#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_sparql(void);

static PyObject* language_func(PyObject *self, PyObject *args) {
    return PyLong_FromVoidPtr(tree_sitter_sparql());
}

static PyMethodDef methods[] = {
    {"language", language_func, METH_NOARGS,
     "Get the tree-sitter language for SPARQL."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "binding",
    "Tree-sitter SPARQL language binding",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_binding(void) {
    return PyModule_Create(&module);
}
