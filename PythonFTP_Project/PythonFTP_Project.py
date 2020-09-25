from ftplib import FTP

with FTP('ftp.example.com', 'anonymous','you email address') as ftp:
    print(ftp.getwelcome())

