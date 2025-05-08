# Function to read the links from a file
def read_links(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Read the two lists from the files
list1 = read_links('list1.txt')
list2 = read_links('list2.txt')

# Find duplicates in each list
duplicates_list1 = [link for link in set(list1) if list1.count(link) > 1]
duplicates_list2 = [link for link in set(list2) if list2.count(link) > 1]

# Find links that are in list1 but not in list2
missing_in_list2 = [link for link in set(list1) if link not in set(list2)]

# Find links that are in list2 but not in list1
missing_in_list1 = [link for link in set(list2) if link not in set(list1)]

# Write the results to results.txt
with open('results.txt', 'w') as f:
    f.write("Duplicates in list 1:\n")
    for link in duplicates_list1:
        f.write(link + "\n")

    f.write("\nDuplicates in list 2:\n")
    for link in duplicates_list2:
        f.write(link + "\n")

    f.write("\nLinks in list 1 but not in list 2:\n")
    for link in missing_in_list2:
        f.write(link + "\n")

    f.write("\nLinks in list 2 but not in list 1:\n")
    for link in missing_in_list1:
        f.write(link + "\n")

print("Results saved to results.txt")