# Setup
Created an image of user\_drive with no partitions using FTK Imager 4.7.1
then loaded image into evidence tree.

# Looking through Recycle Bin:
`$RNFG3Q3.docx` was the only DOCX that seemed properly formatted. Exported and opened, it said:
"I've been thinking about hiding my passwords in plain sight. I learned about this thing called
steghide. Maybe ill use it on  one of my photos".

# Looking on Desktop:
Only thing was `the_secret_key.xlsx` which is password protected.

# Looking in Pictures > iCloud Photos:
Only the `iCloud Photos` folder appeared to have any images. I tried to use `steghide` on one
or two of the photos but wasn't getting anywhere. I assumed I needed to find a password to 
unlock the images and moved on. 

```
 $ steghide info IMG_8397.JPEG
"IMG_8397.JPEG":
  format: jpeg
  capacity: 44.6 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
steghide: could not extract any data with that passphrase!
```

# Looking through Edge history
Edge history is found in `Users\User\AppData\Local\Microsoft\Edge\User Data\Default\History`

```
 $ sqlite3 History
 sqlite> SELECT * FROM urls;
1|file:///C:/Windows/system32/oobe/FirstLogonAnim.html||1|0|13355352995494526|0
2|https://go.microsoft.com/fwlink/?linkid=2132465&form=MT004A&OCID=MT004A|Welcome to Microsoft Edge|2|1|13355353984776401|0
3|https://www.microsoft.com/edge/welcome?form=MT00LJ|Welcome to Microsoft Edge|2|0|13355353984776401|0
4|https://www.microsoft.com/en-us/edge/welcome?ep=296&es=66&form=MT00LJ|Welcome to Microsoft Edge|3|0|13355353985321551|0
5|https://lanceydancey.github.io/df_ctf/|CTF Challenge|1|1|13355354004274338|0
```

The only interesting URL was `lanceydancey.github.io/df_ctf/` so I went there. It asked for a 
password. I looked through the developer console and was able to see the check and get the 
correct password from there.

![dev console](./img/dev-console.png)

The output with the correct password was `DF{and_you_get_an_A!}`. 

![output](./img/output.png)

Looking at the code in the devoloper console felt a little cheat-y, so I went back to the 
photos.

# FAB.jpeg
I decided to start with `FAB.jpeg` this time because when checking the metadata with `exiftool`
this image had much less than the other images. When nothing was entered for the password it
found an embedded file. 

```
 $ steghide info FAB.jpeg
"FAB.jpeg":
  format: jpeg
  capacity: 43.2 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "b64_password.jpg":
    size: 10.8 KB
    encrypted: rijndael-128, cbc
    compressed: yes

 $ steghide extract -sf FAB.jpeg
Enter passphrase:
wrote extracted data to "b64_password.jpg".
```

## Base64
When I opened `b64_password.jpg` it was an image of the text `cHJldHR5Z3JlYXRwYXNzd29yZA==`.
The equal signs at the end along with the name of the file made it clear that it was encoded 
with base64.

```
 $ echo "cHJldHR5Z3JlYXRwYXNzd29yZA==" | base64 --decode
prettygreatpassword
```

### The Secret Key
I tried to use it on the other images but it didn't work, but it did work on 
`the_secret_key.xlsx`.

| The key |
| ------- |
| very\_secret\_key |

