# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# Use system defaults, if available
test -f /sw/bin/init.sh && . /sw/bin/init.sh

PATH=$PATH:/usr/sbin/:/opt/local/bin
export PATH

DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:/usr/lib/boost:/sw/lib/mysql
export DYLD_LIBRARY_PATH

SVN_EDITOR=vi
export SVN_EDITOR

ARCH=`uname -m`;
export ARCH;

Hostname=karro-desk
export HOSTNAME;

alias ssh-redhawk='ssh redhawk.hpc.muohio.edu'

#alias mysql_server = 'sudo /Library/StartupItems/MySQLCOM/MySQLCOM start'
#alias mysql = '/usr/local/mysql'

# If running interactively, then:
if [ "$PS1" ]; then

    # don't put duplicate lines in the history. See bash(1) for more options
    # export HISTCONTROL=ignoredups

    # check the window size after each command and, if necessary,
    # update the values of LINES and COLUMNS.
    shopt -s checkwinsize

    # enable color support of ls and also add handy aliases
    if [ "$TERM" != "dumb" ]; then
        alias ls='ls -G'
	#eval `dircolors -b`
	#alias ls='ls --color=auto'
	#alias dir='ls --color=auto --format=vertical'
	#alias vdir='ls --color=auto --format=long'
    fi

    # some more ls aliases
    #alias ll='ls -l'
    #alias la='ls -A'
    #alias l='ls -CF'


    # set a fancy prompt
    PS1='karro-desk:\w> '

    # If this is an xterm set the title to user@host:dir
    #case $TERM in
    #xterm*)
    #    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'
    #    ;;
    #*)
    #    ;;
    #esac

    # enable programmable completion features (you don't need to enable
    # this, if it's already enabled in /etc/bash.bashrc).
    #if [ -f /etc/bash_completion ]; then
    #  . /etc/bash_completion
    #fi
fi



# Setting PATH for MacPython 2.6
# The orginal version is saved in .bash_profile.pysave
# PATH="/Library/Frameworks/Python.framework/Versions/2.6/bin:${PATH}"
# export PATH

##
# Your previous /Volumes/MacintoshHD2/Users/karroje/.bash_profile file was backed up as /Volumes/MacintoshHD2/Users/karroje/.bash_profile.macports-saved_2011-01-24_at_16:18:04
##

# MacPorts Installer addition on 2011-01-24_at_16:18:04: adding an appropriate PATH variable for use with MacPorts.
export PATH=/opt/local/bin:/opt/local/sbin:$PATH
# Finished adapting your PATH environment variable for use with MacPorts.


# Setting PATH for Python 2.7
# The orginal version is saved in .bash_profile.pysave
# PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
# export PATH

##
# Your previous /Users/karroje/.bash_profile file was backed up as /Users/karroje/.bash_profile.macports-saved_2013-06-05_at_13:58:47
##

# MacPorts Installer addition on 2013-06-05_at_13:58:47: adding an appropriate PATH variable for use with MacPorts.
export PATH=/opt/local/bin:/opt/local/sbin:$PATH
# Finished adapting your PATH environment variable for use with MacPorts.

