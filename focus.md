Yes, you can create a script to add 100px to the width of a PDF page, though it's important to understand how PDF dimensions are measured. The "px" (pixel) measurement common in screen design does not directly translate to PDF's point-based coordinate system, where 1 point is equal to 1/72 of an inch. 
The process involves two steps, which are best handled by a Python library like PyMuPDF (or fitz) or PyPDF2:
1.	Change the page's canvas size: Increase the page's overall dimensions to provide the extra space.
2.	Reposition the original content: Draw the original content onto the new, larger page. 
Here is a script using PyMuPDF, which simplifies the process of creating a new page with updated dimensions and drawing the old content onto it. 
Python script using PyMuPDF
First, install the PyMuPDF library:
pip install PyMuPDF 
