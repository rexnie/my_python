#!/usr/bin/env python
import os
import os.path
import fnmatch
import sys
import shutil
'''
the utility for rename files
usage:
    ./file_rename.py [directory-under-which-to-rename]

    frename=FileRename(work_dir='directory-under-which-to-rename')
    frename.change_postfix(old_postfix='png',new_postfix='jpg') a.png --> a.jpg
work_dir: support absolute/relative directory
the renamed files place under work_dir/temp/

other support methold:
frename.change_postfix(old_postfix='png',new_postfix='jpg') a.png --> a.jpg
frename.add_postfix(self,new_postfix='txt') a --> a.txt
frename.add_prefix(self,prefix='xx',before=True) a.txt --> test_a.txt/ a_test.txt
frename.rename_number(self,prefix='xx') a.txt --> test_001.txt
frename.replace_words(self,oldWord='xx',newWorld='yy'):   abcxxdef.txt --> abcyydef.txt

changelist:
1. init version
2. ignore the program itself, not to process file_rename.py
3. add replace_words methold
4. read argv[1] as directory-under-which-to-rename
'''
class FileRename(object):
    def __init__(self,work_dir='.'):
        self.inited=False
        if os.path.exists(work_dir):
            if os.path.isdir(work_dir):
                #print os.listdir(work_dir)
                if self.mkdir_temp(work_dir):
                    self.file_process_cnt=0
                    self.inited=True
                    self.fn_myself=os.path.basename(os.path.abspath(__file__))
            else:
                print '"%s" is not a dir' % work_dir
        else:
            print '"%s" is not exist' % work_dir

    def mkdir_temp(self,work_dir):
        temp_dir=os.path.join(work_dir,'temp')
        #print work_dir,temp_dir
        if os.path.exists(temp_dir):
            print '%s exist, remove it.' % temp_dir
            shutil.rmtree(temp_dir)

        os.mkdir(temp_dir)
        self.work_dir=work_dir
        self.temp_dir=temp_dir
        return True

    def check_inited(self):
        if not self.inited:
            print 'not inited,quit'
            sys.exit(1)
    def is_myself(self,fn):
        if fn == self.fn_myself:
            return True
        return False
    def change_postfix(self,old_postfix='png',new_postfix='jpg'):
        self.check_inited()
        work_dir=self.work_dir
        cnt=self.file_process_cnt=0
        for fn in os.listdir(work_dir):
            if os.path.isfile(os.path.join(work_dir,fn)) and \
              fnmatch.fnmatch(fn, '*.' + old_postfix): # fnmatchcase for case-sensitive.
                file_root=os.path.splitext(fn)[0]
                file_new=file_root+'.'+new_postfix
                print fn,file_new
                os.rename(os.path.join(work_dir,fn),os.path.join(self.temp_dir,file_new))
                cnt+=1
        self.file_process_cnt=cnt
        print '%s files renamed' % cnt        
    def add_postfix(self,new_postfix='jpg'):
        self.check_inited()
        work_dir=self.work_dir
        cnt=self.file_process_cnt=0
        for fn in os.listdir(work_dir):
            if os.path.isfile(os.path.join(work_dir,fn)) and not self.is_myself(fn):
                file_root=os.path.splitext(fn)[0]
                file_new=fn+'.'+new_postfix
                #print fn,file_new
                os.rename(os.path.join(work_dir,fn),os.path.join(self.temp_dir,file_new))
                cnt+=1
        self.file_process_cnt=cnt
        print '%s files renamed' % cnt        
    def add_prefix(self,prefix='xx',before=True):
        self.check_inited()
        work_dir=self.work_dir
        cnt=self.file_process_cnt=0
        for fn in os.listdir(work_dir):
            if os.path.isfile(os.path.join(work_dir,fn)) and not self.is_myself(fn):
                file_root,file_ext=os.path.splitext(fn)
                if before:
                    file_new=prefix+'_'+file_root+file_ext
                else:
                    file_new=file_root+'_'+prefix+file_ext
                print fn,file_new
                os.rename(os.path.join(work_dir,fn),os.path.join(self.temp_dir,file_new))
                cnt+=1
        self.file_process_cnt=cnt
        print '%s files renamed' % cnt
    def rename_number(self,prefix='xx'):
        self.check_inited()
        work_dir=self.work_dir
        cnt=self.file_process_cnt=0
        for fn in os.listdir(work_dir):
            if os.path.isfile(os.path.join(work_dir,fn)) and not self.is_myself(fn):
                file_root,file_ext=os.path.splitext(fn)
                file_new=prefix+'_'+'{0:04d}'.format(cnt)+file_ext
                print fn,file_new
                os.rename(os.path.join(work_dir,fn),os.path.join(self.temp_dir,file_new))
                cnt+=1
        self.file_process_cnt=cnt
        print '%s files renamed' % cnt

    def replace_words(self,oldWord='xx',newWorld='yy'):
        self.check_inited()
        work_dir=self.work_dir
        cnt=self.file_process_cnt=0
        for fn in os.listdir(work_dir):
            if os.path.isfile(os.path.join(work_dir,fn)) and not self.is_myself(fn) and \
              fnmatch.fnmatchcase(fn,'*'+oldWord+'*'):
                file_new = fn.replace(oldWord,newWorld)
                print fn,file_new
                os.rename(os.path.join(work_dir,fn),os.path.join(self.temp_dir,file_new))
                cnt+=1
        self.file_process_cnt=cnt
        print '%s files renamed' % cnt
    
if __name__ == '__main__':
    work_dir='.'
    if len(sys.argv) == 2:
        work_dir=sys.argv[1]
    fr=FileRename(work_dir)
    fr.replace_words(oldWord='aazenclock3',newWorld="aazenclock2")
