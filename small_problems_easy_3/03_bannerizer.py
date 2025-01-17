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


def print_in_box(text, max_width=76):
    if len(text) <= max_width:
        dashes = '-' * len(text)
        spaces = (' ' * len(text))
        middle = ['| ' + text + ' |']
    else:
        text = text.splitlines()
        dashes = '-' * max_width
        spaces = ' ' * (max_width)
        middle = [('| ' + line.ljust(max_width, ' ')  + ' |') for line in text]
    print('+-' + dashes + '-+')
    print('| ' + spaces + ' |')
    for line in middle:
        print(line)
    print('| ' + spaces + ' |')
    print('+-' + dashes + '-+')

def word_wrap(text, max_width=76):
    if len(text) <= max_width:  # base case: returns final line in recursion
        return text
    else:
        broken_line = text[:max_width + 1].rsplit(' ', 1)
        line = broken_line[0]
        remaining_text = broken_line[1] + text[max_width + 1:len(text)]
        wrapped = line + '\n' + word_wrap(remaining_text, max_width)
        return wrapped

def wrap_in_box(string, max_width=76):  # 76 == 80 minus two chars on each side
    if len(string) <= max_width - 4:    # box adds two chars on each side
        return print_in_box(string)
    else:
        wrapped_text = word_wrap(string, max_width - 4)
        return print_in_box(wrapped_text, max_width - 4)

wrap_in_box("Modify this function so that it truncates the message if it "
            "doesn't fit inside a maximum width provided as a second argument "
            "(the width is the  width of the box itself). You may assume no "
            "maximum if the second argument is omitted. "
            "For a challenging but fun exercise, try word wrapping messages "
            "that are too long to fit, so that they appear on multiple lines "
            "but are still contained within the box. This isnt an easy "
            "problem, but its doable with basic Python.", 60)

wrap_in_box('To boldly go where no one has gone before.')

wrap_in_box('')


# Doesn't work with paragraphs yet due to uneven line break which messes 
# up the first line of the following paragraph. Could fix that in a new 
# version.


# Now that I've done word wrapping the hard way, here's a version using 
# textwrap.wrap(). And it still doesn't work with paragraphs because it
# doesn't seem to observe '\n'.


from textwrap import wrap

def print_in_box(text, max_width=76):
    if type(text) == str:
        dashes = '-' * len(text)
        spaces = (' ' * len(text))
        middle = ['| ' + text + ' |']
    if type(text) == list:
        dashes = '-' * max_width
        spaces = ' ' * (max_width)
        middle = [('| ' + line.ljust(max_width, ' ')  + ' |') for line in text]
    print('+-' + dashes + '-+')
    print('| ' + spaces + ' |')
    for line in middle:
        print(line)
    print('| ' + spaces + ' |')
    print('+-' + dashes + '-+')

def wrap_in_box(text, max_width=76):  # 76 == 80 minus two chars on each side
    if len(text) <= max_width - 4:    # box adds two chars on each side
        return print_in_box(text)
    else:
        wrapped_text = wrap(text, max_width - 4)
        return print_in_box(wrapped_text, max_width - 4)

wrap_in_box("Modify this function so that it truncates the message if it "
            "doesn't fit inside a maximum width provided as a second argument "
            "(the width is the  width of the box itself). You may assume no "
            "maximum if the second argument is omitted. "
            "For a challenging but fun exercise, try word wrapping messages "
            "that are too long to fit, so that they appear on multiple middle "
            "but are still contained within the box. This isnt an easy "
            "problem, but its doable with basic Python.", 60)

wrap_in_box('To boldly go where no one has gone before.')

wrap_in_box('')