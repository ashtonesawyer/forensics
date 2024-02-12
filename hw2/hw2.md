# Summary
This report investigates the hard drive of Booring Soft employee Kevin Tunes. 
There are multiple photos over the course of multiple years of concerts corroponging to dates
when Kevin was supposed to be attending work confrences.
confrenses. Also on multiple occations the browser history shows music reporting sites 
and accessing Spotify, a music streaming service. 

# Purpose
This investigation's purpose was to examine Kevin Tunes hard drive for evidence of 
non-compliance with Booring Soft policies during the work day and attendance of company-paid
trips to confrences. 

# Methodology
The disk was imaged using dc3dd and mounted to a Kali linux virtual machine (VM) using mount. 
Image and PDF metadata was examined using exiftool. DOCX matadata was viewed by exporting 
the document as a zip of XML files and examining with xmllint. Web browser history was viewed
through the applications' SQLite databases.

The disk was mounted using a loop device in read-only and no-execution mode. The loop device
allowed accessing the file system as normal. The read-only and no-execution modes are important
to ensure that the drive image was not altered in any while while it was being accessed. 

# Findings
## Images
- `01.jpg` was taken 2011-10-6 as 14:58:09 at 35 deg 2' 43.80" N, 90 deg 1' 22.80" W 
  (Graceland Mansion in Memphis, TN) on an Apple iPhone 4.
- `04.jpg` was taken 2011-10-6 21:21:53 at 38 deg 36' 54.00" N, 90 deg 11' 45.60" W 
  (Fairview Heights, IL) on an Apple iPhone 4. The photo is of a woman on stage 
  playing the guitar.
- `05.jpg` was taken 2012-6-8 14:20:40 on an Apple iPhone 4S. The photo is of a band 
  onstage at an outdoor concert.
- `06.jpg` was taken 2012-6-8 19:50:30 on an Apple iPhone 4S. The photo is of a band 
  onstage at an outdoor concert. 
- `07.jpg` was taken 2011-3-21 22:37:37 on an Apple iPhone 4. The photo is of a band on 
  stage. 
- `08.jpg` was taken 2011-7-16 15:44:29 on a Canon PowerShot SD1100 IS. The photo is of a 
  band on stage at an outdoor concert.
- `09.jpg` was taken 2012-6-9 16:14:27 on an iPhone 4S. The photo is of a band on stage 
  at an outdoor concert. 
- `10.jpg` was taken 2012-6-9 16:27:10 on an iPhone 4S. The photo is of a banch on stage
  at an outdoor concert. 
- `11.jpg` was taken 2012-7-15 20:33:37 at 41 deg 53' 3.60" N, 87 deg 39' 54.60" W
  (Union Park in Chicago, IL) on an Apple iPhone 4S. The photo is of a concert. 
- `12.jpg` was taken 2012-7-14 21:17:00 at 41 deg 52' 59.40" N, 87 deg 40' 1.20" W 
  (near Union Park in Chicago, IL) on an Apple iPhone 4S. The photo is of a concert.

## PDFs
- `098108749117.pdf` was created 2014-3-3 13:00:22 (UTC-06:00) with iText 2.1.0. It is a ticket
  to Pitchfork Music Festival.
- `11291307605-327242879-ticket.pdf` was created 2014-9-23 10:03:15 (UTC-07:00) by Eventbrite. 
  It is a ticket to Pygmalion Festival. 
- `My Favorite Bands.pdf` was created  2015-6-30 13:58:58 (UTC) from 
  Microsoft Word - My Favorite Bands.docx. 

## DOCX
`My Favorite Bands.docx` wsa created 2015-6-30 13:44:00 (UTC) by Kevin Tunes in Microsoft
Macintosh Word.

## Firefox Data
**Browsing on 2015-6-30:**
- 08:04:42 - search for pitchfork
- 08:05:17 + 08:05:29 - on pitchfork.com
- 08:11:54 - search for pitchfork
- 08:11:57 - 08:13:33 - on pitchfork.com
- 08:13:46 - search for stereogum
- 08:13:57 + 08:14:27 - on stereogum.com
- 08:14:39 - search for Spotify
- 08:14:46 + 08:15:01 - on spotify.imusic-go.com
- 08:15:54 - on spotify.com
- 08:16:22 - on stereogum.com
- 08:16:22 - 08:16:45 - quickconnect redirects to stereogum.com
- 08:16:47 - 08:18:02 - on spotify.com/us/signup
- 08:18:04 - 08:18:09 - on spotify.com/us/download and download.spotify.com
- 08:20:46 - 08:21:02 - on play.spotify.com
- 08:25:31 - 08:29:14 - on stereogum.com

**Cookies data on 2015-6-30:**
- 08:05:26 - google wallet
- 08:13:41 - newhive (social media)
- 08:14:27 - stereogum
- 08:16:09 - pitchfork
- 08:17:07 - spotify
- 08:22:02 - pitchfork
- 08:22:16 - spotify
- 08:23:20 - pitchfork
- 08:24:00 - adobe
- 08:24:09 - spotify
- 08:24:13 - pitchfork
- 08:24:36 - play.spotify
- 08:27:11 - youtube
- 08:27:34 - twitter
- 08:27:51 - bandcamp
- 08:29:24 - stereogum
- 08:30:09 - stereogum

**Searchbar history on 2015-6-30:**
- 08:11:52 - "pitchfork"
- 08:15:50 - "spotify"

# Conclusions
My finding show that Kevin's computer was used to browse the internet and stream music during
the work day, both of which are against company policy. There are photos on the drive 
taken at concerts at times when Kevin was supposed to be attending work conferences.
Tickets to music festivals were downloaded and a PDF was created from a word document delcaring 
favorite bands during work hours.  
