
# pyspy

This repo, pyspy, is under construction.

It should contain more software when I present it to the Python Meetup 2016-01-18:

http://www.meetup.com/BayPIGgies/events/227481217

Until then, pyspy is under construction.

I intend for pyspy to run on Ubuntu 14 so I give instructions for installing and operating pyspy on Ubuntu 14.

If you want to run pyspy on a Mac I assume that you could easily generate and then follow instructions to run pyspy on a Mac.

If you want to run Ubuntu 14 as a guest inside your Mac, you can find information on the web for setting that up:

http://www.google.com/search?q=How+to+run+Ubuntu+as+Guest+of+Mac+OSX+with+VirtualBox+or+VMware+or+Parallels+or+Vagrant

Once you find good information, you will probably need a copy of Ubuntu 14:

http://releases.ubuntu.com/14.04/ubuntu-14.04.3-desktop-amd64.iso

If you want to run Ubuntu 14 as a guest of Windows I know that it is possible but be prepared for bad Windows behavior. For example I recently saw a windows10-virtualbox installation that failed to support copy-paste with a mouse.

# Install pyspy on Ubuntu 14

I like to install a wide variety of software on my Ubuntu host.  Some of the software listed below is probably not necessary but I like to have it available.

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install autoconf bison build-essential libssl-dev libyaml-dev \
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3       \
libgdbm-dev libsqlite3-dev gitk postgresql postgresql-server-dev-all  \
libpq-dev emacs wget curl chromium-browser openssh-server aptitude    \
ruby ruby-dev sqlite3

sudo apt-get update
sudo apt-get upgrade
```

I like to install pyspy into this folder:

/home/ann/pyspy

You could try to install it elsewhere.

Anyway, I do this:

```
useradd ann -m -s /bin/bash
passwd ann
ssh -YA ann@localhost
```

Next I clone pyspy from github.com:

```
cd ~
git clone https://github.com/danbikle/pyspy
```

Then I install Anaconda Python:

```
cd ~
curl https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Linux-x86_64.sh > Anaconda3-2.4.1-Linux-x86_64.sh
bash Anaconda3-2.4.1-Linux-x86_64.sh
cd ~/anaconda3/bin
mv curl curl_ana
cd ~
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
python
quit()
```

# Operate pyspy

I operate pyspy by running a shell script at 12:50pm California time:

```
~/pyspy/bin/noon50.bash
```

Sometimes I will run pyspy at night after the most recent closing price is available:

```
~/pyspy/bin/night.bash
```

After pyspy runs, it will place files in this folder:

```

```





