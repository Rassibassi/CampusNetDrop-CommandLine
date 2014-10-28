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