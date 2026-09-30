# Day 29 - Password Manager GUI 🔐

## 📌 Project

A simple Password Manager application built using **Python** and the **Tkinter** library.

The application allows users to save website login details, generate random passwords, and automatically copy generated passwords to the clipboard.

## 🧠 What I Learned

- Building a GUI application using **Tkinter**
- Working with Tkinter `Canvas`, `Label`, `Entry`, and `Button` widgets
- Creating layouts using the `grid()` geometry manager
- Using `columnspan` to span widgets across multiple columns
- Setting the initial focus on an `Entry` widget
- Using `messagebox` for pop-up dialogs
- Using `showinfo()` to display information
- Using `askokcancel()` to request user confirmation
- Reading user input from Entry widgets using `.get()`
- Clearing Entry widgets using `.delete()`
- Generating random passwords using the `random` module
- Using list comprehensions to generate password characters
- Using `random.choice()` to select random characters
- Using `random.shuffle()` to randomise password characters
- Joining characters into a string using `"".join()`
- Saving data to a text file using file handling
- Using append mode with `open(..., "a")`
- Copying generated passwords to the clipboard using `pyperclip`
- Working with external Python modules
- Organising a larger GUI application into functions

## 💻 Project Features

- 🔐 Password Manager GUI
- 🌐 Website input field
- 📧 Email/username input field
- 🔑 Password input field
- 🎲 Random password generator
- 📋 Automatically copies generated passwords to the clipboard
- 💾 Saves website, email, and password information to a text file
- ⚠️ Checks for empty required fields
- 💬 Confirmation pop-up before saving
- 🧹 Clears the website and password fields after saving
- 🎨 Custom logo displayed using Tkinter Canvas

## 🎯 What I Practiced

This project helped me build a more complete GUI application using Tkinter.

I practiced creating structured layouts using `grid()`, working with dialog boxes, generating random passwords, handling user input, saving information to a file, and interacting with the system clipboard.

I also practiced combining multiple Python modules such as `random`, `tkinter`, `messagebox`, and `pyperclip` in a single application.

## 📂 Project Structure

```text
Day - 29 - Password Manager/
│
├── main.py
├── logo.png
├── data.txt
└── README.md
```

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**