@echo off

set sikuli_jar=%SIKULI_HOME%\sikuli-script.jar

set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

jybot --pythonpath=example.sikuli ^
      --outputdir=results ^
      --loglevel=TRACE ^
      %*