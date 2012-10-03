#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  untitled.py
#
#  Copyright 2012 Clean ubuntu 11.10 <ptr@ubuntu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import os, errno
import shutil
import glob
import subprocess
#Global functions, consider adding to an outside class

def iterate_folder(path, ftype="*"):
    """
    """
    f_list = []
    for f in glob.glob( os.path.join(path, ftype) ):
        f_list.append(f)
    return f_list

class PDF_Proc:
    """Global Variables:
    """
    #Class constants
    #required folder dictionary
    txt_dir = "txt_output/"
    proc_dir = "processed/"
    ocr_dir = "ocr_req/"
    curr_dir = os.getcwd() + '/'

    #member variables
    folders = { "txt_dir": txt_dir, "proc_dir":proc_dir, "ocr_dir":ocr_dir }

    def __init__(self):
        """
        """
        print "init"

    def run_PDFToText(self, directory=curr_dir):
        """
        """

      #if folder exists, delete all files
        #create folder
        for f in self.folders.keys():
            self.folders[f] = directory + self.folders[f]
            if os.path.isdir(self.folders[f]):
                shutil.rmtree(self.folders[f])
            self.mkdir_p(self.folders[f])

        files = iterate_folder(directory, "*.pdf")
        for file in files:
            basename = os.path.basename(file)
            f_txt_name =  directory + basename[:-3] + "txt"
            task = subprocess.Popen(['pdftotext', '-enc', 'ASCII7', file])
            task.wait()
            shutil.move(f_txt_name, self.folders['txt_dir'])

        txt_files = os.listdir(self.folders['txt_dir'])
        for tfile in txt_files:
            t_path = self.folders['txt_dir'] + tfile
            size = os.path.getsize( t_path )
            if size > 200:
                shutil.copyfile( t_path, self.folders['proc_dir'] )
            else:
                txt_name = os.path.basename(tfile)
                pdf_name = txt_name[:-3] + "pdf"
                shutil.copyfile( directory + pdf_name, self.folders['ocr_dir'] + pdf_name )

    def run_PDFTK(self, directory):
        """
        """
        print ""
#        task = subprocess.Popen(['pdftk',
    def mkdir_p(self, path):
        """
        """
        try:
            os.makedirs(path)
        except OSError as esc:
            if exc.errno == errno.EEXIST:
                pass
            else:
                raise

pdf_proc = PDF_Proc()
pdf_proc.run_PDFToText( )
