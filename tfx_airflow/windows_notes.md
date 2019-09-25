# Windows Notes

Windows is a bit challenging to use, but it's possible to make it work.  These notes should help.

* Must use Windows 10 Pro or better (Not home version)
* Use the *Git Bash* tool (aka MINGW64) which comes with Git for Windows to run the host_start.sh script
* Make sure that Docker is set for using Linux containers
* Share the drive in Docker settings 
* Open ports (if necessary) 445, 8080, 8888. 6006
* Edit c:\windows\system32\drivers\etc\hosts on Windows and add
    127.0.0.1 localunixsocket.local
* Terminal is messed up
    * no prompt
    * really narrow
    * ... but it actually works.  Type commands carefully.
