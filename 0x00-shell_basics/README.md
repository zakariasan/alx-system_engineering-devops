# 0x00 Shell Basics

![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)


## :astronaut: Resources

- [What is "the Shell"?](http://linuxcommand.org/lc3_lts0010.php).
- [Navigation](http://linuxcommand.org/lc3_lts0020.php).
- [Looking Around](http://linuxcommand.org/lc3_lts0030.php).
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php).
- [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php).
- [Working With Commands](http://linuxcommand.org/lc3_lts0060.php).
- [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html).
- [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/).
- [Have Fun ]().

## :desktop_computer:  Tasks

* [0.Where am I?](./0-current_working_directory) : Write a script that prints the absolute path name of the current working directory.

* [1.What's in there?](./1-listit) : Display the contents list of your current directory.

* [2.There is no place like home](./2-bring_me_home) : Write a script that changes the working directory to the user’s home directory.

* [3.The long format](./3-listfiles) : Display current directory contents in a long format

*  [4.Hidden files](./4-listmorefiles) : Display current directory contents, including hidden files (starting with `.`). Use the long format.

*  [5.I love numbers](./5-listfilesdigitonly) : Display current directory contents.

*  [6.Welcome](./6-firstdirectory) : Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

*  [7.Betty in my first dir](./7-movethatfile) : Move the file betty from `/tmp/` to `/tmp/my_first_directory`.

*  [8.Bye bye Betty](./8-firstdelete) : Delete the file `betty`.

* [9.Bye bye My fDir](./9-firstdirdeletion) :Delete the directory `my_first_directory` that is in the `/tmp/` directory.

* [10.Back to the future](./10-back) : Write a script that changes the working directory to the previous one.
 
* [11.Lists](./11-lists) : Write a script that lists all files in long format.

* [12.File type](./12-file_type): Write a script that prints the type of the file named `iamafile`. The file iamafile will be in the `/tmp/` directory when we will run your script.

* [13.We are symbols, and inhabit symbols](./13-symbolic_link) : Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
 
* [14.Copy HTML files](./14-copy_html)  : Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

## :abacus: Advanced_part

* [15.Let's move](./100-lets_move) : Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

* [16.Clean !Emacs.vim](./101-clean_emacs): Create a script that deletes all files in the current working directory that end with the character `~`.
 
* [17.Tree](./102-tree) : Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.
 
* [18.Life is a series of commas, not periods](./103-commas) : Write a command that lists all the files and directories of the current directory, separated by commas (`,`).

* [19.File type: magic world](./school.mgc) : Create a magic file `school.mgc` that can be used with the command `file` to detect School data files. `School` data files always contain the string `SCHOOL` at offset 0.
