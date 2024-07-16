# PY101-109 Small Problems, Easy 3, Problem 3. "Bannerizer":

"""Write a function that takes a short line of text and prints it 
within a box.

Example 1:
print_in_box('To boldly go where no one has gone before.')

Output for Example 1:
+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

Example 2:
print_in_box('')

Output for Example 2:
+--+
|  |
|  |
|  |
+--+

You may assume the output will always fit in your terminal window.
"""


def print_in_box(string):
    horizontal_edge = '+' + ('-' * (len(string) + 2)) + '+'
    horizontal_edge_padding = '|' + (' ' * (len(string) + 2)) + '|'
    print(horizontal_edge, horizontal_edge_padding, sep = '\n')
    print('| ' + string + ' |')
    print(horizontal_edge_padding, horizontal_edge, sep = '\n')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')


"""Further Exploration:

Modify this function so that it truncates the message if it doesn't fit 
inside a maximum width provided as a second argument (the width is the 
width of the box itself). You may assume no maximum if the second 
argument is omitted.

For a challenging but fun exercise, try word wrapping messages that are 
too long to fit, so that they appear on multiple lines but are still 
contained within the box. This isn't an easy problem, but it's doable 
with basic Python.
"""


def print_in_box(string, max_width=76):
    if len(string) <= max_width:
        horizontal_edge = '+' + ('-' * (len(string) + 2)) + '+'
        horizontal_edge_padding = '|' + (' ' * (len(string) + 2)) + '|'
        print(horizontal_edge, horizontal_edge_padding, sep='\n')
        print('| ' + string + ' |')
        print(horizontal_edge_padding, horizontal_edge, sep='\n')
    else:
        lines = string.splitlines()
        horizontal_edge = '+' + ('-' * (max_width + 4)) + '+'
        horizontal_edge_padding = '|' + (' ' * (max_width + 4)) + '|'
        print(horizontal_edge, horizontal_edge_padding, sep='\n')
        for line in lines:
            print('| ' + line.ljust(max_width + 2, ' ')  + ' |')
        print(horizontal_edge_padding, horizontal_edge, sep='\n')

def word_wrap(string, max_width=76):
    if len(string) <= max_width:
        return string
    else:
        line = string[0 : max_width]
        remainder = string[max_width:len(string)]
        wrapped = line + '\n' + word_wrap(remainder, max_width)
        return wrapped
        # line = string[0 : max_width]   # do a git branch
        # line = line[0 : line.rfind(' ')]
        # remainder = string.removeprefix(line).strip(' ')
        # wrapped = line + '\n' + word_wrap(remainder, max_width)
        # return wrapped
        # results in endless loop

def wrap_in_box(string, max_width=76): # 76 = 80 minus two chars on each side
    if len(string) <= max_width:
        return print_in_box(string)
    else:
        wrapped_text = word_wrap(string, max_width)
        return print_in_box(wrapped_text)


wrap_in_box('For a challenging but fun exercise, try word wrapping messages '
            'that are too long to fit, so that they appear on multiple lines '
            'but are still contained within the box. This isnt an easy '
            'problem, but its doable with basic Python.')

# just have to change word_wrap() to wrap on the words instead of chars,
# do this by comparing len words joined and maxwidth

        # words = string.split()
        # line = ''
        # for word in words:
        #     while len(line) <= max_width:
        #         line += words.pop(word.index(word)) + ' '
        # print(line)
        # # line = string[0 : max_width] + '\n'
        # remainder = string[max_width:len(string)]
        # wrapped = line + word_wrap(remainder, max_width)
        # return wrapped

        # line = string[0 : max_width] + '\n'
        # line = line[0 : line.rfind(' ')] + '\n'
        # remainder = string.removeprefix(line)
        # wrapped = line + word_wrap(remainder, max_width)
        # return wrapped
        # results in endless loop

        # Version that works:
    #     def word_wrap(string, max_width=76):
            # if len(string) <= max_width:
            #     return string
            # else:
            #     line = string[0 : max_width] + '\n'
            #     remainder = string[max_width:len(string)]
            #     wrapped = line + word_wrap(remainder, max_width)
            #     return wrapped