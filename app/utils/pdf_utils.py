import fitz
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF (primary) 
    with fallback to pdfplumber
    
    Args:
        pdf_path: Path to the PDF file
    
    Returns:
        str: Extracted text content
    """
    try:
        # Try with PyMuPDF first (faster)
        text = ""
        with fitz.open(pdf_path) as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
        
        # If text extraction was successful and not empty
        if text.strip():
            return text
        
        # If PyMuPDF didn't extract text properly, try pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        
        return text
    
    except Exception as e:
        # Log the error and return a message
        print(f"Error extracting text from PDF: {str(e)}")
        return f"Error extracting text from PDF: {str(e)}"