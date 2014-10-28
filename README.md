CampusNetDrop CommandLine
=========================
This is a tiny application to synchronize the shared files of your courses, projects and groups from DTU CampusNet to your personal computer. After configuration of your login and your courses, the application will be able to download the shared files of these courses with the same structure as online. Every time you re-run the downloader it will check for new versions of already downloaded files and of course download new files.

![Alt text](img.jpg?raw=true "Folder structure")

This is the command line version for experienced users.

Download or clone the application files into a directory.

Run the configuration:

```python /pathToDirectory/configuration.py```

Run the download:

```python /pathToDirectory/downloader.py```

The code is Python 2.7

Tip 1: In order to download files of old courses, navigate into the archive on CampusNet and tick the desired courses.

Tip 2: Add a `alias` in your `~/.bashrc` or `~/.bash_profile` for faster access

#Configuration example Linux and OSX
```CampusNet username? (sXXXXXX)
sxxxxxx
CampusNet password?
Password: 
Configure courses? (yes/no)
yes
Add "Courses --- 01426 Cryptology 2" to Downloads? (y/n)
y
Where to download the "01426 Cryptology 2" files? (Path)
/home/UserName/DTU/Cryptology
Add "Courses --- 02457 Non-Linear Signal Processing" to Downloads? (y/n)
y
Where to download the "02457 Non-Linear Signal Processing" files? (Path)
/home/UserName/DTU/Non-Linear Signal Processing
Add "Groups --- International MSc students" to Downloads? (y/n)
n
Add "Groups --- Master students" to Downloads? (y/n)
n```

#Configuration example Windows
```CampusNet username? (sXXXXXX)
sxxxxxx
CampusNet password?
Password: 
Configure courses? (yes/no)
yes
Add "Courses --- 01426 Cryptology 2" to Downloads? (y/n)
y
Where to download the "01426 Cryptology 2" files? (Path)
C:/DTU/Cryptology
Add "Courses --- 02457 Non-Linear Signal Processing" to Downloads? (y/n)
y
Where to download the "02457 Non-Linear Signal Processing" files? (Path)
C:/DTU/Non-Linear Signal Processing
Add "Groups --- International MSc students" to Downloads? (y/n)
n
Add "Groups --- Master students" to Downloads? (y/n)
n```