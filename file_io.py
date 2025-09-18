# message = 'Hello, world!'

# # open a file named test.txt
# # file name is "test.txt" (or whatever you choose)
# # 'w' means "write mode"
# # the CSCE104 is unique to me (Prof Bailey)
# file = open("CSCE104/test.txt", 'w')
# # write that message to the file
# file.write(message)
# # close the file every time!!!
# file.close()

# # alter the message
# message = '\nHere is an edit'
# # shortcut version:
# # with open will automatically call 'close' for us
# # because I'm still in write mode, this will overwrite the file
# # with open("CSCE104/test.txt", 'w') as file:
# # because this is in append mode, the new message will be added to the end
# with open("CSCE104/test.txt", 'a') as file:
#     file.write(message)


# month_conv = {
#     "Jan":"January",
#     'Feb':'February',
#     'Mar':'March',
#     'Apr':'April',
#     'May':'May',
#     'Jun':'June',
#     'Jul':'July',
#     'Aug':'August',
#     'Sep':'September',
#     'Oct':'October',
#     'Nov':'November',
#     'Dec':'December'
# }
# # name of the file, file mode
# # ignore the subfolder
# with open('CSCE104/dictionary.txt', 'w') as file:
#     file.write( str(month_conv) )


# # file name is 'test.txt'
# # ignore the 'CSCE104/'
# with open('CSCE104/test.txt', 'r') as file:
#     # I know the file is small, to read() is safe
#     contents = file.read()
#     print(contents)

# # TODO: read the dictionary from the file
# #       and then use it like a dictionary
# # ignore the CSCE104
# with open('CSCE104/dictionary.txt', 'r') as read_file:
#     contents = read_file.read()
#     print(contents)
#     print( type(contents) )     # should be 'str' for 'string'
#     # TODO: convert 'str' to 'dictionary' 'dict'
#     # eval function attempts to convert a string back to whatever it was before
#     # 1. take the string called "contents" and try to eval it
#     # 2. store whatever it finds in the variable "new_dict"
#     new_dict = eval(contents)
#     print(new_dict)
#     print( type(new_dict) )     # hoping for 'dictionary' or 'dict'

#     # use new_dict like a dictionary
#     print('Month {} means {}'.format( 'Feb', new_dict['Feb'] ))


# open a file, to read from it
# BUT: the file does not exist, so this WILL FAIL
# hw2 = open('test123.txt', 'r')
# print(hw2.read())
# hw2.close()

# handle this using a try-except
try:
    hw2 = open('test123.txt', 'r')
    print(hw2.read())
    hw2.close()
except FileNotFoundError:
    print('Sorry, I could not find that file')


import io
try:
    # mistakenly open the file in WRITE mode, but try to READ from it
    hw2 = open('test123.txt', 'w')
    print(hw2.read())
    hw2.close()
except io.UnsupportedOperation:
    print('The file is in write mode. It cannot be read')
