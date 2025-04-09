📦 DataStructureManager

A Python package to manage and interact with core data structures like Arrays, Lists, Stacks, Queues, and more. This project is part of a class assignment to demonstrate understanding of data structure concepts and their implementation in Python.

🚀 Features

✅ Array implementation with common operations
✅ Singly and doubly linked lists
✅ Stack (LIFO) with push/pop operations
✅ Queue (FIFO) with enqueue/dequeue support
✅ Circular Queue, Priority Queue (optional extension)
✅ Modular, reusable codebase
✅ Well-documented and easy to use
🛠️ Installation

Clone the repository:

git clone https://github.com/yourusername/DataStructureManager.git
cd DataStructureManager
Then, install the package locally (if you turned it into a proper package):

pip install .
📚 Usage

from datastructuremanager import Stack, Queue, LinkedList

# Stack example
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # Output: 20

# Queue example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1

# Linked List example
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.display()  # Output: 5 -> 10
📁 Project Structure

DataStructureManager/
│
├── datastructuremanager/
│   ├── __init__.py
│   ├── array.py
│   ├── stack.py
│   ├── queue.py
│   ├── linkedlist.py
│   └── utils.py
│
├── tests/
│   ├── test_stack.py
│   └── test_queue.py
│
├── README.md
└── setup.py
🎯 Goals

Implement classic data structures from scratch
Understand underlying algorithms and time complexities
Provide a unified and simple interface for each structure
👩‍💻 Author

Your Name
Course Name / Professor
Your GitHub
📄 License

This project is licensed under the MIT License.

