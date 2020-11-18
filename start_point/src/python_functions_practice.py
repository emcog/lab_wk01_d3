def return_10():
    return 10

# adding 2 argument & store in variable called result


def add(first_number, second_number):
    return first_number + second_number

add(1, 2)


def subtract(first_number, second_number):
    return first_number - second_number

subtract(10, 5)


def multiply(first_number, second_number):
    return first_number * second_number

multiply(4, 2)

def divide(first_number, second_number):
    return first_number / second_number

divide(10, 2)


# find the length of sting, use the appropriate method 
# appx len(string), function which accepts string as string as argument and runs len(string)

def length_of_string(string):
    return len(string)

length_of_string('A string of length 21')

# add two strings together
# define a function which accepts two strings as arguments and return string 1 + 2

def join_string(string_1, string_2):
    return(string_1 + string_2)

join_string('Mary had a little lamb, ', 'its fleece was white as snow')


# create function which takes decimal numbers entered
# as a string and complete a mathmetical function on those numbers
def add_string_as_number(xx, yy):
    return int(xx) + int(yy)
    

add_string_as_number('1', '2')



# create a function which refers to a list of months of the year and pulls the correct name of the year when a numerical month is entered
# this function will access the index of the list, we will predefine this list but a more advanced program would pull this from elsewhere e.g. google calendar

months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def number_to_full_month_name(numerical_month):
    return(months_of_year[numerical_month - 1])

number_to_full_month_name(1)

number_to_full_month_name(3)

number_to_full_month_name(9)

# create a function which accepts an int as an argument and corresponds to list of the months of the year and shorten the month to first 3 letters

def number_to_short_month_name(numerical_month):
    # get the correct month
    # shorten the correct month
    return months_of_year[numerical_month - 1][0:3]

number_to_short_month_name(1)

number_to_short_month_name(4)

number_to_short_month_name(10)