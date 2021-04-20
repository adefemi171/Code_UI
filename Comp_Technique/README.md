# COMPILING TECHNIQUES

## Problem 1
1. Design a Lexical Analyzer in a particular PL to analyze another PL.

## Solution 1
1. 
Change to the directory on your computer (if you are not already there):

```
cd Problem_1
```
For this Problem I designed the analyzer using Python and the PL am analyzing is written in Golang.
- To run the Golang flie do:
```
go run fileSample.go
```
PS: You can install Golang usong this [help](https://golang.org/dl/)
- To run analyzer:
```
python lexer.py
```
The output is saved into a .txt file and also displayed in the terminal.

## Problem 2
1. Write a program to receive an infix arithmetic expression to postfix notation and get the value of the expression.

## Solution 1
1. Used Python for this problem for both conversion of Infix to Postfix notation and also evaluated the expression

- To run this program:
```
python infixToPostfix.py
```

Example of an infix expreesion you can pass:
```
3*(2+1)-2/2
```
The output is displayed in the terminal.

