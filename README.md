Google Photos - Drive sync
===========================

## Why?

We love to store all of our photos in Google Photos.

We like to have them also available in Google Drive, so we can manage them in a folder like 
structure and sync them with our local storage.

I used to have a manically curated folder structure, with dates and events for my
photo archive, but in Google Drive all the photos, no matter if they are in an album
are seen with the <year>/<month> structure, nothing more. Not nice!

This script purpose is to sync the Google Photos album structure to Google Drive,
useful and easy. 

## TODO:

This is all in development, so the quick summary here is: everything.

After spending some time with the available Google Photos API (PicasaWeb API)
unfortunately only old albums created in Picasa are returned.
So we should probably use un-official APIs or wait for a better future. 

Meanwhile, there are other things to do:
I would like to sync with a local folder outside Google Drive,
so that everything in Google Drive is saved locally, but only images
after a certain ages are synced back online (I have 100GB of online storage and much more media).
