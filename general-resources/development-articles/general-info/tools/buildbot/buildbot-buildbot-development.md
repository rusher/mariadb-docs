
# Buildbot Development

## Developing on the Buildbot code


Buildbot has all of the right ideas for solving the problem of maintaining a complex codebase like MariaDB at a high level of quality. However, there are some smaller fixes and extensions we need to develop on the Buildbot code.


Here I describe how I set up an environment for hacking on the buildbot code. Readers beware, I am a Perl guy, so this may not reflect how a Python person would choose to do things.


First I installed the virtualenv Python package:


```
tar zxf virtualenv-1.3.3.tar.gz 
cd virtualenv-1.3.3/
mkdir -p /home/knielsen/python/lib/python/
PYTHONPATH="$HOME/python/lib/python" python setup.py install --home="$HOME/python"
cd ..
PYTHONPATH="$HOME/python/lib/python" ~/python/bin/virtualenv sandbox
```

Then I cloned the latest BuildBot tree from the Git repository:


```
git clone git://github.com/djmitche/buildbot.git
cd buildbot/
```

Install the BuildBot code in the virtualenv sandbox in development mode and run the test suite.


(The virtualenv stuff has a script sandbox/bin/activate that is the recommended way to use things. However, I really dislike keeping that kind of state in the shell, since it means shell commands (for example copy-pasted from history) will behave differently depending on when and where they are run. That is the reason for passing the PYTHONPATH directly on the command line.)


```
PYTHONPATH="$HOME/python/lib/python" ~/devel/buildbot/sandbox/bin/python setup.py develop
PYTHONPATH="$HOME/python/lib/python" ~/devel/buildbot/sandbox/bin/python /usr/bin/trial buildbot.test
```

*[I get the error "error: Could not find suitable distribution for Requirement.parse('Twisted==2.5.0')" on the first of these commands, but things seem to work ok anyway (I installed all buildbot dependencies via Ubuntu apt-get packages).]*


Once that works, one can install a master and a slave and start them running each in their own terminal window for easy access to log:


```
cd ..
PYTHONPATH="$HOME/python/lib/python" sandbox/bin/buildbot create-master master
cp buildbot/contrib/bzr_buildbot.py master/
# Edit master/master.cfg as appropriate
cd master
PYTHONPATH="$HOME/python/lib/python" ../sandbox/bin/python /usr/bin/twistd --nodaemon --no_save -y buildbot.tac

cd ..
PYTHONPATH="$HOME/python/lib/python" sandbox/bin/buildbot create-slave slave localhost:9989 test testpass
# Edit slave/info/* as appropriate
cd slave
PYTHONPATH="$HOME/python/lib/python" ../sandbox/bin/python /usr/bin/twistd --nodaemon --no_save -y buildbot.tac
```

With this I was able to hack away at the code and just restart the master and slave to test stuff. The web status pages will be on [](https://localhost:8010/)


## See also


* [BuildBot ToDo](buildbot-todo.md)


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
