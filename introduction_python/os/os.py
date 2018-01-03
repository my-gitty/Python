fout = open('oops.dean', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

# --------------------- OS ----------------------#

import os

# judging whether the file or dirctory exists or not
os.path.exists('oops.dean')
os.path.exists('.')

name = 'oops.dean'
os.path.isfile(name)
os.path.isdir(name)

# judging whether the name is absolute path or not
os.path.isabs(name)

# ----------- shutil ----------#

import shutil
shutil.copy(name,'ohno.dean')

# ----------- shutil ----------#

# rename from name1 to rename1
name1='ohno.dean'
rename1 = 'ohwell.dean'
os.rename(name1, rename1)

# hard link the name to the hard_link_name
try:
	hard_link_name = 'yikes.dean'
	os.link(name, hard_link_name)
	os.path.isfile(hard_link_name)
except:
	pass

#symbol link the name to the symbol_link_name
try:
	symbol_link_name = 'jeepers.dean'
	os.symlink(name, symbol_link_name)
	os.path.islink(symbol_link_name)
except:
	pass

# change the mode
os.chmod(name, 0o400)

import stat
os.chmod(name, stat.S_IRWXU)
###################################################
"""
stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IWOTH: 其他用户有写权限0o002
stat.S_IROTH: 其他用户有读权限0o004
stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
stat.S_IXGRP: 组用户有执行权限0o010
stat.S_IWGRP: 组用户有写权限0o020
stat.S_IRGRP: 组用户有读权限0o040
stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
stat.S_IXUSR: 拥有者具有执行权限0o100
stat.S_IWUSR: 拥有者具有写权限0o200
stat.S_IRUSR: 拥有者具有读权限0o400
stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
stat.S_IREAD: windows下设为只读
stat.S_IWRITE: windows下取消只读
"""
##################################################

# change the ower
try:
	uid = 5
	gid = 22
	os.chown(name, uid, gid)
except:
	pass

# obtain the path absolutely
print(os.path.abspath(name))

#obtain the path of symbol link
os.path.realpath(symbol_link_name)

# delete a file
os.remove(hard_link_name)

# make a dirctory
os.mkdir('poem.dean')

# list the dirctory
print(os.listdir('poem.dean'))

# change the dirctory now to another
os.chdir('.')

# delete a dirctory
os.rmdir('poem.dean')

import glob
print(glob.glob('o*'))



# --------------------- OS ----------------------#



