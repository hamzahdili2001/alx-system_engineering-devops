# Command: echo
The `echo` command is used to display text or the values of variables in the terminal.

Example:
echo "Hello, World!"
This will display the text "Hello, World!" in the terminal.

# Command: cat
The `cat` command is used to concatenate and display the contents of one or more files in the terminal.

Example:
cat file.txt
This will display the contents of the file `file.txt` in the terminal.

# Command: head
The `head` command is used to display the first N lines of a file in the terminal. By default, it displays the first 10 lines.

Example:
head -n 5 file.txt
This will display the first 5 lines of the file `file.txt` in the terminal.

# Command: tail
The `tail` command is used to display the last N lines of a file in the terminal. By default, it displays the last 10 lines.

Example:
tail -n 5 file.txt
This will display the last 5 lines of the file `file.txt` in the terminal.

# Command: find
The `find` command is used to search for files in a directory hierarchy.

Example:
find / -name "file.txt"
This will search for the file named `file.txt` starting from the root directory (`/`).

# Command: wc
The `wc` command is used to count the number of lines, words, and characters in a file.

Example:
wc file.txt
This will display the line count, word count, and character count of the file `file.txt` in the terminal.

# Command: sort
The `sort` command is used to sort the contents of a file in ascending or descending order.

Example:
sort file.txt > sorted_file.txt
This will sort the contents of the file `file.txt` and save the sorted result in a new file named `sorted_file.txt`.

# Command: uniq
The `uniq` command is used to remove or identify duplicate lines in a file.

Example:
sort file.txt | uniq > unique_file.txt
This will sort the contents of the file `file.txt` and remove any duplicates, saving the result in a new file named `unique_file.txt`.

# Command: grep
The `grep` command is used to search for a specific pattern in a file or input.

Example:
grep "Hello" file.txt
This will search for the pattern "Hello" in the file `file.txt` and display all lines that contain the pattern.

# Command: tr
The `tr` command is used to translate or delete characters from a file or input.

Example:
tr '[:lower:]' '[:upper:]' < file.txt
This will translate all lowercase characters in the file `file.txt` to uppercase and display the result in the terminal.

# Command: rev
The `rev` command is used to reverse the order of characters in each line of a file or input.

Example:
rev file.txt
This will reverse the order of characters in each line of the file `file.txt` and display the result in the terminal.

# Command: cut
The `cut` command is used to extract specific columns
