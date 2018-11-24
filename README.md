#Logs Analysis Project - Udacity
####Full Stack Web Development ND
---------

###About

This log analysis project is part of Udacity Full Stack Nano Degree. It is for streching python,relational database, complex queries skills and etc. In general it is **internal reporting tool** to fictional news website database that contains: 
* `The authors table`: includes information about the authors of articles.
* `The articles table`: includes the articles themselves.
* `The log table`: includes one entry for each time a user has accessed the site.
#####the reporting tool answers this three questions
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
--------------

##Getting Started
in order to run this application you will need database software -linex virtual machine- and the data to work on.

###Prerequisites
follow these steps one by one:
*install python 3 from [python official site ](https://www.python.org/downloads/)
*install [virtual box ](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
*install Vagrant [download it from vagrantup.com](https://www.vagrantup.com/downloads.html).
*Download the row data that used in this project [Download data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).


###Installing

#####Install VirtualBox
VirtualBox is the software that actually runs the virtual machine.[Download here virtual box ](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
#####Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

>Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.


If Vagrant is successfully installed, you will be able to run `vagrant --version`   in your terminal to see the version number.



#####Start the virtual machine
######NOTE:
>make directory or run this `mkdir log_analys` and `cd /log_analys`.

From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it.
> This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!


######Logged in!
>If you are now looking at a shell prompt that starts with the word vagrant congratulations — you've gotten logged into your Linux VM.

#####Download the data
Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.


#####Views used

######Status Total

```
create view d2 as (select split_part(time::text,' ',1)d, count(*)  from log group by d);
```

######Status failed

```
create view d1 as (select split_part(time::text,' ',1)d, count(*)  from log where status != '200 OK'  group by d;
```




