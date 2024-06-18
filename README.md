# Forensics
This is a backup of my homework from Digital Forensics (CS493 - Winter 24) that was originally 
hosted on GitLab. The main markdown file in each folder is the report from each case, including 
reason for investigation, methods, findings, and conclusions. 

Below is a breif description of the different homeworks. 

## HW1 - VM Setup
I set up a WSL Kali linux VM to use for course work. 

## HW2 - Metadata
I images, mounted, and explored a disk image, looking primarily at different files' metadata
and web history. 

## HW3 - File Carving
I looked for JPEGs on a formated drive both manually using `dd`, as well as 
automatically with `photorec` and `foremost`. I then used the GPS data from the extracted
images to create an interactive map. 

## HW4 - Timeline Analysis
I used Sleuth Kit tools and Plaso to create a timeline of device activity and FTK Imager to 
recover deleted files. 

## Final
I started with an unfamiliar NTFS image and explored it both mounted and using FTK Imager. 
The goal was to get a CTF key using all of the strategies taught in the class. 
