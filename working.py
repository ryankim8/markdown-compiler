# Temp file for work


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    accumulator = ""
    has_opened = False # meaning: Have we seen a star yet
    if line.count("*") % 2 == 1:
        return line
    for char in line:
        if char == "*":
            if not has_opened:
                accumulator += "<i>"
                has_opened = True
            else:
                accumulator += "</i>"
                has_opened = False
        else:
            accumulator += char
    return accumulator