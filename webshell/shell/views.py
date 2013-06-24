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
    if request.method == 'POST':
        dirname = request.POST.get('path')
        url = request.get_full_path() + dirname
    if dirname == os.getcwd():
        url = request.get_full_path() + dirname
    directory, files, directories = backshell.list_dir(dirname) if type(backshell.list_dir(dirname)) == type(()) else ('Error!!',['come back'],['cant read the directory {0}'.format(dirname)])
    return render_to_response('cd.html',
                              {'shell':{'directory': directory,
                               'files': files,
                               'directories': directories},
                              'full_path': url
                              },
                              context_instance=RequestContext(request)
                              )



def remove_file(request, filename):
    """Removes the file.

    Keyword arguments:
    filename (str)      --  the full path to file (default '')

    """
    status = backshell.remove_file(filename)
    return redirect('cd', os.path.split(filename)[0])


def remove_directory(request, dirname):
    """Removes the directory.

    Keyword arguments:
    dirname (str)       --  the full path to directory (default '')

    """
    status = backshell.remove_dir(dirname)
    return redirect('cd', os.path.split(dirname)[0])


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