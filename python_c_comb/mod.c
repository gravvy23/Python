#include <Python.h>
void sort(long* tab, long size){
    long tmp; 
    do {
        for (int i = 0; i < size -1; ++i){
            if (tab[i] > tab[i+1]){
                tmp = tab[i];
                tab[i] = tab[i+1];
                tab[i+1] = tmp;
            }
        }
        size--;
    } while (size > 0);
}

long dzielnik(long a, long b){
    long min = a;
    long dzielnik = 1;
    if (b < a) min = b;
    for (int i = 2; i <= min; ++i){
        if (a%i == 0 && b%i == 0) dzielnik = i;
    }
    return dzielnik;
}
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a=0,b=0,c=0;
	if(!PyArg_ParseTuple(args, "i|ii", &a, &b, &c)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/3.4/c-api/arg.html
		//docs.python.org/3.4/c-api/concrete.html
		//docs.python.org/3.4/c-api/object.html
		//docs.python.org/3.4/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", a+b+c);
}

static PyObject *bubble_sort(PyObject *self, PyObject *args){
    PyObject *list;
    if(!PyArg_ParseTuple(args, "O", &list)){ //jezeli do stringa wstawi sie | to po sa opcjonalne    
        return NULL;
    }
    long size = PyList_Size(list);
    long tab[size];
    PyObject *tmp;
    for (long i = 0; i < size; ++i){
        tmp = PyList_GetItem(list,i);
        tab[i] = PyLong_AsLong(tmp);
    }
    sort(tab,size);

    PyObject *nlist;
    nlist = PyList_New(size);

    Py_ssize_t pos = 0;
    for(long i=0; i < size; ++i)
    {
        PyObject *value = PyLong_FromLong(tab[i]);
        PyList_SetItem(nlist,pos,value);
        pos++;
    }

    return Py_BuildValue("O", nlist);
}

static PyObject *zad2(PyObject *self, PyObject *args){
    PyObject *dict;
    if(!PyArg_ParseTuple(args, "O", &dict)){ //jezeli do stringa wstawi sie | to po sa opcjonalne    
        return NULL;
    }
    PyObject *tuple =  PyTuple_New(PyDict_Size(dict));
    long tmp1, tmp2, tmp3;
    PyObject *key, *value;
    PyObject *ToTuple;
    Py_ssize_t pos = 0, pos2 = 0;


    while (PyDict_Next(dict, &pos, &key, &value)) {
        tmp1 = PyLong_AsLong(value);
        tmp2 = PyLong_AsLong(key);
        tmp3 = dzielnik(tmp1,tmp2);
        ToTuple = PyLong_FromLong(tmp3);
        PyTuple_SetItem(tuple,pos2, ToTuple);
        pos2 +=1;
    }
    return Py_BuildValue("O", tuple);
}
//PyDict_next
//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
    {"BubbleSortC", (PyCFunction)bubble_sort, METH_VARARGS, "Bubble sort"},
    {"zad2", (PyCFunction)zad2, METH_VARARGS, "zad 2"},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
