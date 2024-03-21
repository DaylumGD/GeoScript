## Definitive statements

# #define:
syntax: #define varname: type = value

# #include:
syntax: #include moduleorlib

# #export:
syntax: #export object from moduleorlib

# #function:
syntax: #function my_function(args) {}

## Controll flow

# if statements
syntax: if (value comp value) {
    >> code
}

# if else statements
syntax: if (value comp value) {
    >> code
} else {
    >> code
}

# if else if statements
syntax: if (value comp value) {
    >> code
} else if (value comp value) {
    >> code
}

## Loops
# while loops
Syntax: while (condition) {
    >> code
}

# for loops
Syntax: for (declaredvar, condition, method) {
    >> code
}

# forEach loops
Syntax: forEach (declaredvar, itirable_data_struct) {
    >> code
}

## Structule statements

# @container
Syntax: @container(percentfrom, percentto) {
    >> code
}

# @structure
Syntax: @structure my_strcut {
    >> code
}

# @class
Syntax: @class my_class {
    >> code
}

## Types

# int

# float

# str

# array

# group

# collision

# counter

# dict

# collection

# nulltype

# auto

# codeblock