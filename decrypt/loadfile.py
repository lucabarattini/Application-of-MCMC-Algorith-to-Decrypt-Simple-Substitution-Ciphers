def _readfile(path):
    '''
    This function is used to open and read a text file.

    Parameters
    ----------
    path : str
        the path of the text we want to read and return
    '''
    f = open(path, "r")
    text = f.read()
    f.close()
    return text