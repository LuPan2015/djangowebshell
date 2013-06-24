#-------------------------------------------------------------------------------
# Name:        shell
#
# Author:      iBiZoNiX
#
# Created:     20.06.2013
#
# Copyright:   (c) iBiZoNiX 2013
#-------------------------------------------------------------------------------

"""The module allows you to file management.
Available methods:
info
os_info
list_dir
read_file
make_file
make_dir
remove_file
remove_dir
rename
search

"""

import os
import sys
import shutil


def os_info():
    """Returns tuple with version of python and platform type of os."""

    return(sys.version, sys.platform)


def list_dir(dirname=os.getcwd()):
    """Returns tuple (scanned directory, files, directories).

    Keyword arguments:
    dirname (str)       --  full path to directory (default 'os.getcwd()')

    """

    if not os.path.exists(dirname):
        result = 'Directory not found'
    else:
        if os.path.isdir(dirname):
            result = (dirname,
                      #list of files
                      [x for x in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, x))],
                      #list of directories
                      [x for x in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, x))]
                      )
        else:
            result = '{0} is not a directory'.format(dirname)

    return result


def read_file(filename):
    """Returns the contents of the file.

    Keyword arguments:
    filename (str)      --  full path to file (default '')

    """

    if not os.path.exists(filename):
        result = '"{0}" not found'.format(filename)
    else:
        if os.path.isfile(filename):
            try:
                #returns all contents of the file
                result = ' '.join(((line for line in open(filename))))
            except:
                result = 'Error opening "{0}"'.format(filename)
        else:
            result = '"{0}" is not a file'.format(filename)

    return result


def make_file(filename, contents=''):
    """Creates a new file.

    Keyword arguments:
    filename (str)      --  full path to file (default '')
    contents (str)      --  contents of file (default '')

    """

    if os.path.exists(filename):
        result = '"{0}" already exists'.format(filename)
    else:
        try:
                opfile = open(filename,'w')
                opfile.write(contents)
                opfile.close()
                result = '"{0}" successfully created'.format(filename)
        except:
                result = 'Error creating "{0}"'.format(filename)

    return result


def make_dir(dirname):
    """Creates a new dir.

    Keyword arguments:
    dirname (str)       --  full path to directory (default '')

    """

    if os.path.exists(dirname):
            result = '"{0}" already exists'.format(dirname)
    else:
            try:
                os.mkdir(dirname)
                result = '"{0}" successfully created'.format(dirname)
            except:
                result = 'Error creating "{0}"'.format(dirname)

    return result


def remove_file(filename):
    """Removes the file.

    Keyword arguments:
    filename (str)      --  full path to file (default '')

    """

    if os.path.exists(filename):
        try:
            os.remove(filename)
            result = '"{0}" successfully removed'.format(filename)
        except:
            result = 'Error removing "{0}"'.format(filename)
    else:
        result = '"{0}" not found'.format(filename)

    return result


def remove_dir(dirname):
    """Removes the directory.

    Keyword arguments:
    dirname (str)       --  full path to directory (default '')

    """

    if os.path.exists(dirname):
        try:
            shutil.rmtree(dirname)
            result = '"{0}" successfully removed'.format(dirname)
        except:
            result = 'Error removing "{0}"'.format(dirname)
    else:
        result = '"{0}"  not found'.format(dirname)

    return result


def rename(old_name, new_name):
    """Renames file or directory.

    Keyword arguments:
    old_name (str)      --  full path to old name of file or directory (default '')
    new_name (str)      --  full path to new name of file or directory (default '')

    """

    if os.path.exists(old_name):
            try:
                os.rename(old_name,new_name)
                result = 'The dir/file "{0}" successfully renamed'.format(old_name)
            except:
                result = 'Error renaming "{0}"'.format(old_name)
    else:
            result = '"{0}" not found'.format(old_name)

    return result


def search(dirname, search_object):
    """Just search.

    Keyword arguments:
    dirname (str)       --  full path to directory for search (default '')
    search_object (str) --  a sought-for object (default '')

    """

    db = [] #list of scanned directory
    result = [] #list of such object
    if not os.path.exists(dirname):
        result = '"{0}"  not found'.format(dirname)
    else:
        def scan(dir):
            try:
                files = os.listdir(dir)
            except WindowsError:
                return
            for file in files:
                if os.path.isfile(dir+file):
                    db.append(dir+file)
                elif os.path.isdir(dir+file):
                    db.append(dir+file)
                    scan(dir+file+'/')
            return db
        for path in scan(dirname):
            if search_object.upper() in os.path.split(path)[1].upper():
                result.append(path)
        if result == '':
            result = '"{0}" not found'.format(search_object)
    return result

