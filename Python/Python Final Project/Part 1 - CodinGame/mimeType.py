"""
MIME types are used in numerous internet protocols to associate a media type (html, image, video ...)
with the content sent. The MIME type is generally inferred from the extension of the file to be sent.

This program  makes it possible to detect the MIME type of a file based on its name.
"""

mimes = {}  # Generate hash table

n = int(input())  # Entries amount
q = int(input())  # Data amount

for i in range(n):
    mime = input().split()
    mimes[mime[0].lower()] = mime[1]  # Assign input data into dict; Case sensitive

for j in range(q):
    fname = input().split(".")  # Split with period, list
    if len(fname) != 1:  # Determine length of file name list
        print(mimes.get(fname[-1].lower(), "UNKNOWN"))  # Case sensitive
    else:
        print("UNKNOWN")
