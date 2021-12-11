#include "iostream"
#include "string"
#include "fstream"
#include "vector"
#include "stdexcept"
#include "cstdlib"
#include "cassert"
#include "time.h"
#include "cstring"
using namespace std;

class MyStack;
class MyNode
{
    public:
    friend class MyStack;

    MyNode(const int& d): _value(d), _left(this), _right(this) {}

    friend ostream& operator<< (ostream &out, MyNode* myNode);
    friend ostream& operator<< (ostream &out, MyStack* myStack);

    private:
    int      _value;
    MyNode*  _left;
    MyNode*  _right;
};


ostream& operator<< (ostream &out, MyNode* myNode)
{
    out << "Node" <<  myNode->_value << "";
    return out;
}

class MyStack
{
public:
    MyStack() { _root = new MyNode(-1); _num_element=0;}
    ~MyStack() { clear(); }
    void pop() {
        if(_num_element==0){
            throw invalid_argument( "Can not execute pop() on an empty stack" );
        }
        else{
            _num_element -= 1;
            
            // ---TODO:
            // Connect the second last element >> root
            // Connect root >> the second last element
            // ---
            MyNode* sec = (_root->_left)->_left;
            delete sec->_right;
            _root->_left = sec;
            sec->_right = _root;
        }
    }
    void push(MyNode* node) {
        _num_element += 1;
        
        // ---TODO:
        // Connect the last element >> inserted node
        // Connect the inserted node >> root
        // ---
        MyNode* last = _root->_left;
       	last->_right = node;

        node->_right = _root;
       	node->_left = last;
       	
       	_root->_left = node;
    }

    void clear() {
        MyNode* temp = _root->_right;
        MyNode* temp2 = temp->_right;
        while (temp!= _root){
            delete temp;
            temp = temp2;
            temp2 = temp2->_right;
        }
        delete _root;
    }

    friend ostream& operator<< (ostream &out, MyStack* myStack);

private:
    MyNode*  _root;
    int _num_element;

};

ostream& operator<< (ostream &out, MyStack* myStack)
{
    MyNode* node = myStack->_root->_right;
    while(node != myStack->_root){
        out << ">>" << node;
        node=node->_right;
    }
    return out;
}



vector<string> split_string(string s) {
    vector<string> v;
    string temp = "";
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == ' ') {
            v.push_back(temp); temp = "";
        } else {
            temp.push_back(s[i]);
        }
    }
    v.push_back(temp);
    return v;
}



int main(int argc, char** argv) {
    clock_t tStart = clock();
    string ifile_name="input_1.txt";
    string ofile_name="";
    string mem_str="mem";
    int index;
    bool has_ofile = false;
    ifstream ifile;
    ofstream ofile;
    vector<string> args(argv, argv + argc );
    if (argc == 3){
         ifile_name=args[1];
         ofile_name=args[2];
         has_ofile=true;
    }
    else if(argc == 2){
         ifile_name=args[1];
    }
  	ifile.open(ifile_name.c_str());
    if(has_ofile){
         ofile.open(ofile_name.c_str());
    }
    if ((index = ifile_name.find(mem_str, 0)) != string::npos){
        printf("Please press any key to start\n");
        cin.ignore();
        printf("start..\n");
    }
    string str;
    MyStack * myStack = new MyStack;
    while (getline(ifile, str)) {
        vector<string>v = split_string(str);
        if( v[0] =="PUSH"){
            int myVal = atoi(v[1].c_str());
            MyNode* myNode = new MyNode(myVal);
            myStack->push(myNode);
        }
        else{
            myStack->pop();
        }
        if(has_ofile){
            ofile << myStack <<"\n";
        }
    }
    if(has_ofile){
        ofile.close();
    }
    delete myStack;
    if ((index = ifile_name.find(mem_str, 0)) != string::npos){
        printf("Please press any key to exit\n");
        cin.ignore();
        printf("end..\n");
    }
    if (has_ofile == false){
        printf("stack.cpp run time of %s: %.5fs\n", ifile_name.c_str(), (double)(clock() - tStart)/CLOCKS_PER_SEC);
    }
    return 0;
}
