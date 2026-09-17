# Day 24 - Mail Merge Project 📄✉️

## 📌 Project

A simple Mail Merge program built using **Python** that reads names from a file and creates personalised letters for each person using a template.

The project uses file handling, directories, and file paths to read input files and generate multiple personalised output files.

## 🧠 What I Learned

- Opening, reading, and writing files using Python
- Using the `with` keyword for file handling
- Reading file contents using `read()` and `readlines()`
- Writing data to files using `write()`
- Using relative file paths
- Understanding absolute and relative paths
- Working with directories and nested folders
- Creating and accessing files inside different directories
- Using `strip()` to remove unwanted whitespace
- Using `replace()` to personalise text
- Using loops to process multiple names
- Creating multiple output files programmatically
- Organising files and folders within a Python project
- Reading and writing data between different files

## 💻 Project Features

- 📄 Reads a letter template from a file
- 👥 Reads a list of names from a file
- ✏️ Creates a personalised letter for each name
- 📁 Organises input and output files into directories
- 🔄 Automatically generates multiple letters
- 💾 Saves each personalised letter as a separate text file

## 📂 Project Structure

```text
Day - 24 - Mail Merge Project/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── example.txt
│       ├── letter_for_Aang.txt
│       ├── letter_for_Appa.txt
│       └── ...
│
├── main.py
└── README.md