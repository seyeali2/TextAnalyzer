# Text Analyzer

## Description

Text Analyzer is a Python application that loads text files and performs different text analysis operations. The project demonstrates object-oriented programming and advanced Python concepts such as regular expressions, generators, decorators, JSON serialization, list comprehensions, lambda expressions, and custom exceptions.

The application also stores analysis results in a JSON archive and allows users to retrieve and filter previous analyses.

---

## Features

* Load a text file
* Count the number of words
* Display the most common words
* Search for patterns using regular expressions
* Display words one by one using a generator
* Display long words (more than 4 characters)
* Save analysis results to a JSON archive
* Store multiple versions of analyses
* Filter archived analyses by word count
* Handle custom exceptions

---

## Project Structure

### main.py

Contains the menu system and user interaction.

### analyzer.py

Contains the `TextAnalyzer` class and all text analysis methods.

### analysis_result.py

Contains the `AnalysisResult` class responsible for:

* storing analysis results
* saving results to the archive
* loading the archive
* filtering archived analyses

### decorator.py

Contains the `validate_text` decorator that prevents analysis when no file has been loaded.

### exceptions.py

Contains custom exceptions:

* FileError
* NoFileLoadedError
* InvalidPatternError

### data.txt

Example text file used for analysis.

### results.json

JSON archive storing analysis history.

---

## Concepts Used

### Object-Oriented Programming

* TextAnalyzer class
* AnalysisResult class
* Constructors (`__init__`)
* Instance attributes

### File Handling

* open()
* with statement

### Exception Handling

* try
* except
* raise
* custom exceptions

### Regular Expressions

* re.findall()

### Generators

* yield

### Lambda Expressions

* lambda item: item[1]

### List Comprehensions

* [word for word in self.text.split() if len(word) > 4]

### Decorators

* @validate_text

### JSON Serialization

* json.dump()
* json.load()

### Static Methods

* @staticmethod

---

## How to Run

1. Place one or more text files in the project folder.
2. Run:

python main.py

3. Use the menu options to analyze text files and manage the archive.

---

## Author

s35049
