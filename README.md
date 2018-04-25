# PDF-Merge

Merge PDF files, quickly and easily.

 - Created to ease work for black book generation for my BE project.
 - Was working with heavy PDF files.
 - Initially using [pdfmerge](www.pdfmerge.com).
 - Required upload of large files, constrained by limited network connection.
 - After upload, got message saying files were too big, need to shift to "premium" version.
 - Wrote code to same effect.

## Advantages
 - No upload of confidential files.
 - Significantly faster.

## Disadvantages
 - Files need to be in alphabetic order.
 - Files need to be in same folder.
 - No drag and drop.

## Setup
  ```
  pip install -r requirements.txt
  ```
## Running script
 - Add files to be merged in alphabetic order to a separate folder
 - Copy M.py to that folder
 - Run M.py

```
 python M.py
```
- Saves `mergedfile.pdf` in the same folder
