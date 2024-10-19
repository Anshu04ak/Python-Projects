# Python Mini Projects
Welcome to the **Python Mini Projects** repository! This repository contains a collection of small and practical projects developed using Python. These projects are designed to showcase various concepts and techniques that can be applied to solve real-world problems using Python programming.

### Introduction
This repository is a compilation of mini projects, each focusing on different aspects of Python development, including but not limited to:

#### **Simple Calculator -** A basic calculator to perform arithmetic operations.
**How it works:**
1. The calculator provides options to add, subtract, multiply, or divide.
2. It takes two numeric inputs from the user and performs the chosen operation.
3. The division function checks for division by zero to avoid errors.
4. The program runs in a loop, allowing the user to perform multiple calculations until they choose to exit.

#### **To-Do List App -** A command-line to-do list manager to keep track of tasks.
**How it works:**
1. *Load/Save Tasks:* The tasks are saved to a file (todo_list.json), and they are loaded every time the app starts, so tasks persist across sessions.
2. *Add Task:* Allows you to add a new task to the list. Each task has a completed status which is initially set to False.
3. *Remove Task:* Removes a task from the list based on the task number.
4. *Mark Task Complete:* Marks a task as completed by selecting its number.
5. *View All Tasks:* Displays all the tasks in the list, showing their status as either "Pending" or "Done."

#### **Number Guessing Game -** A fun game where the user has to guess a randomly generated number.
**How it works:**
1. *Random Number Generation:* The program generates a random number between 1 and 100 using random.randint().
2. *User Input:* The user is prompted to guess the number. If the guess is too high or too low, the program provides feedback.
3. *Attempts Counter:* The program keeps track of how many guesses it takes for the user to find the correct number.
4. *Play Again Option:* After each game, the user is asked if they want to play again.

#### **Password Generator -** A tool to generate strong and secure passwords.
**How it works:**
1. The password contains a mix of:
  1. Lowercase letters (a-z)
  2. Uppercase letters (A-Z)
  3. Digits (0-9)
  4. Special characters (like !, @, #, etc.)
2. The script ensures that the password has at least one character from each category, improving security.
3. The length of the password is specified by the user, and it must be at least 6 characters to ensure strength.
4. The final password is shuffled to randomize the order of characters.

#### **Contact Book -** A command-line application to manage personal contacts.
**How it works:**
1. *Contacts storage:* The contacts are stored in a JSON file (contacts.json) to ensure that they are saved between sessions.
2. *Add Contact:* You can add a new contact with name, phone number, and email.
3. *View Contact:* You can view a contact's details by entering their name.
4. *Update Contact:* You can update an existing contact's phone number or email.
5. *Delete Contact:* You can delete a contact by name.
6. *List All Contacts:* You can list all the saved contacts.
7. *Exit:* The program will loop until you choose to exit.
   
#### **Movie Collection -** This program uses a list of tuples to represent each movie and a dictionary to categorize the movies by genre.
**How it works:**
1. *Add Movie:* Adds a new movie to the collection by specifying the title, genre, and year.
2. *Remove Movie:* Removes a movie from the collection by searching for the title.
3. *Search Movie:* Allows the user to search for a movie by its title and displays its genre and release year.
4. *Sort Movies by Year:* Displays the movies sorted by their release year.
5. *Categorize Movies by Genre:* Categorizes the movies by genre using a dictionary where the genre is the key and the value is a set of movies in that genre.
6. *Count Unique Genres:* Displays the number of unique genres in the collection.
