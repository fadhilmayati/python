# Created by Fadhil Mayati
# Date 17 February 2023


import os
import PyPDF2
import docx

# Get the PDF file path from the user
pdf_file_path = input("Enter the full path of the PDF file to convert: ")

try:
    # Open the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
        # Read the PDF contents
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()
        pdf_text = []
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            pdf_text.append(page.extractText())

    # Join the PDF text into a single string
    pdf_text = '\n'.join(pdf_text)

    # Create a new Word document
    doc = docx.Document()

    # Add the PDF text to the Word document
    doc.add_paragraph(pdf_text)

    # Save the Word document
    docx_file_name = os.path.splitext(pdf_file_path)[0] + '.docx'
    doc.save(docx_file_name)
    print(f"File saved as {docx_file_name}")

except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
except PyPDF2.utils.PdfReadError:
    print("Error: Failed to read the PDF file. Please ensure the file is not corrupted or encrypted.")
except Exception as e:
    print(f"Error: An unexpected error occurred. Details: {str(e)}")
