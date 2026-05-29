#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "hotkey.h"

static PyObject* start_hotkey(PyObject* self, PyObject* args) {
    int fsmodifier;
    int fskey;
    PyObject* pycallback;
    int flag = PyArg_ParseTuple(args, "iiO:create_hotkey", &fsmodifier, &fskey, &pycallback);
    if (!flag) {
        return NULL;
    }
    start_hotkey_listener(fsmodifier, fskey, pycallback);
    return Py_None;
}

static PyObject* stop_hotkey(PyObject* self, PyObject* args) {
    stop_hotkey_listener();
    return Py_None;
}

static PyMethodDef HotkeyModuleMethods[] = {
    {"start_hotkey", (PyCFunction)start_hotkey, METH_VARARGS, PyDoc_STR("start_hotkey(fsmodifier:int, fskey:int, callback:function) -> None")},
    {"stop_hotkey", (PyCFunction)stop_hotkey, METH_VARARGS, PyDoc_STR("stop_hotkey() -> None")},
    {NULL, NULL, 0, NULL}
};

PyDoc_STRVAR(module_doc, "Quickup Hotkey C++ module");

static struct PyModuleDef hotkeymodule = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "hotkeymodule",
    .m_size = 0,
    .m_methods = HotkeyModuleMethods,
};

PyMODINIT_FUNC PyInit_hotkeymodule(void) {
    return PyModuleDef_Init(&hotkeymodule);
}
