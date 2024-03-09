import easyocr

def extract_text_from_image(image_path):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read the image and extract text
    result = reader.readtext(image_path)

    # Extract text from the result
    extracted_text = ' '.join([text[1] for text in result])

    return extracted_text.strip()