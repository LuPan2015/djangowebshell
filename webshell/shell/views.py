import os
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from shell import backshell


def main(request):
    """Redirect to  view 'cd'"""

    return redirect('cd')


def cd(request, dirname=os.getcwd()):
    """Passes through directories

    Keyword arguments:
    dirname (str)       --  goes to a directory (defoult'os.getcwd')

    """
    url = request.get_full_path()
    sort = 'default'
    if request.method == 'POST':
        sort = request.POST.get('sort', 'default')
        if 'path' in request.POST:
            dirname = request.POST.get('path')
            url = request.get_full_path() + dirname
    if dirname == os.getcwd():
        url = request.get_full_path() + dirname
    directory, files, directories = backshell.list_dir(dirname) if type(backshell.list_dir(dirname)) == type(()) else ('Error!!',['come back'],['cant read the directory {0}'.format(dirname)])

    if sort == 'default':
        all_files = directories + files
    elif sort == 'by files':
        all_files = files + directories
    elif sort == 'by folders':
        all_files = directories + files
    elif sort == 'by folders name':
        all_files = directories + files
    elif sort == 'by modify':
        all_files = files + directories
        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(dirname, x)))
        all_files.reverse()
    return render_to_response('cd.html',
                              {'shell':{'all_files': all_files,
                               'directory': directory,
                               'directories': directories,
                               'files': files,
                               'full_path': url}},
                              context_instance=RequestContext(request),
                              )


def uplink(request, dirname):
    """Return a previous directory.

    Keyword arguments:
    dirname (str)       --  the full path to directory (default '')

    """
    return redirect('cd', os.path.split(dirname)[0])

def remove(request, filename):
    """Removes the file or directory.

    Keyword arguments:
    filename (str)      --  the full path to the file (default '')

    """
    if os.path.isfile(filename):
        status = backshell.remove_file(filename)
    elif os.path.isdir(filename):
        status = backshell.remove_dir(filename)
    return redirect('cd', os.path.split(filename)[0])


def new_file(request, dirname):
    """Creates a new file.

    Keyword arguments:
    dirname (str)      --  the path where the file will be created (default '')

    """
    if request.method == 'POST':
        fname = request.POST.get('fname')
        fcontent = request.POST.get('fcontent')
        backshell.make_file(os.path.join(dirname, fname), fcontent)
    return redirect('cd', dirname)


def new_directory(request, dirname):
    """Creates a new directory.

    Keyword arguments:
    dirname (str)      --  the path where the directory will be created (default '')

    """

    if request.method == 'POST':
        dname = request.POST.get('dname')
        backshell.make_dir(os.path.join(dirname, dname))
    return redirect('cd', dirname)