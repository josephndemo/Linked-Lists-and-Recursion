from linked_list import LinkedList

if __name__ == "__main__":
    """
    Create a LinkedList instance and perform recursive operations.
    """

    # 1) Create a LinkedList instance
    employee_ids = LinkedList()

    # 2) Insert sample data
    employee_ids.insert_at_end(101)
    employee_ids.insert_at_end(205)
    employee_ids.insert_at_end(309)
    employee_ids.insert_at_end(412)

    # 3) Display the list
    print("Original List:")
    employee_ids.display()

    # 4) Recursive sum
    total = employee_ids.recursive_sum()
    print("Sum of IDs:", total)

    # 5) Recursive search
    target = 309
    found = employee_ids.recursive_search(target)
    print(f"Search for {target}:", found)

    # 6) Reverse recursively
    employee_ids.recursive_reverse()
    print("Reversed List:")
    employee_ids.display()