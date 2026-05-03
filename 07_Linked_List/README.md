# 🔗 Singly Linked List Implementation in Python

A custom implementation of a **Singly Linked List** built from scratch. Unlike standard Python lists (dynamic arrays), this structure uses nodes and pointers to manage memory, allowing for efficient insertions and deletions without shifting elements.

## 🚀 Key Features
*   **Dynamic Memory:** No pre-allocation required; nodes are created as needed.
*   **CRUD Operations:** Complete support for Creating, Reading, Updating, and Deleting nodes.
*   **Pythonic Magic:** Overloaded `__len__`, `__getitem__`, and `__str__` for a native Python feel.
*   **Index-Based Access:** Support for both value-based and index-based manipulation.

---

## 🛠️ Method Documentation

### 1. Insertion (Create)
| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| `insert_head(value)` | Adds a new node at the very beginning of the list. | $O(1)$ |
| `insert_at_last(value)` | Appends a node to the end by traversing the list. | $O(n)$ |
| `insert_at_index(index, value)`| Inserts a node at a specific numerical position. | $O(n)$ |
| `insert_after(after, value)` | Finds a node by value and inserts a new node immediately after it. | $O(n)$ |

### 2. Retrieval & Search (Read)
| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| `search(value)` | Returns the index position of the first node containing the specified value. | $O(n)$ |
| `__getitem__(index)` | Allows array-style access (e.g., `print(LL[2])`) to retrieve data. | $O(n)$ |
| `__len__()` | Returns the total count of nodes currently in the list. | $O(1)$ |
| `__str__()` | Provides a visual representation of the list (e.g., `1 -> 2 -> 3`). | $O(n)$ |

### 3. Deletion (Delete)
| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| `del_head()` | Removes the first node and updates the head reference. | $O(1)$ |
| `del_tail()` | Navigates to the second-to-last node to remove the final node. | $O(n)$ |
| `del_value(value)` | Locates a specific value and removes its node by re-linking pointers. | $O(n)$ |
| `clear()` | Resets the list to an empty state. | $O(1)$ |

### 3. Some Other Methods 
- `max()` , `reverse()`

---

## 💻 Quick Start
```python
# Create the list object
LL = Linked_List()

# Add nodes
LL.insert_head(3)        # [3]
LL.insert_head(2)        # [2 --> 3]
LL.insert_at_last(4)     # [2 --> 3 --> 4]

# View the list
print(LL)                # Output: 2 --> 3 --> 4
print(f"Length: {len(LL)}") # Output: Length: 3

# Delete and Search
LL.del_value(3)
LL.search(4)             # Output: 1
