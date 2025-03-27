# '''important code'''
# import fitz  # PyMuPDF
# from PIL import Image
# import pytesseract
# import torch
# from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
# import numpy as np
# import re
# import io
# import os
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk import pos_tag

# # Create images directory if it doesn't exist
# def create_images_directory():
#     if not os.path.exists('images'):
#         os.makedirs('images')
#         print("Created 'images' directory")

# # Function for image captioning
# def predict_step(images):
#     processed_images = []
#     for image in images:
#         resized_image = image.resize((224, 224))  # Resize to match model input size
#         np_image = np.array(resized_image)
#         if np_image.shape[-1] != 3:  # Ensure 3 channels (RGB)
#             np_image = np_image[..., :3]
#         processed_images.append(np_image)

#     processed_images = [Image.fromarray(img) for img in processed_images]

#     pixel_values = feature_extractor(images=processed_images, return_tensors="pt").pixel_values
#     pixel_values = pixel_values.to(device)

#     output_ids = model.generate(pixel_values, **gen_kwargs)

#     preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
#     preds = [pred.strip() for pred in preds]
#     return preds

# # Extract text using OCR (Tesseract)
# def extract_text_from_image(image):
#     pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
#     extracted_text = pytesseract.image_to_string(image)
    
#     # Clean extracted text
#     clean_text = re.sub(r'[^\w\s]', '', extracted_text)
#     clean_text = re.sub(r'\d+', '', clean_text)
    
#     return clean_text

# # Text Analysis (Tokenization, POS Tagging)
# def analyze_text(text):
#     sentences = sent_tokenize(text)
#     nouns = []
#     verbs = []
#     adjectives = []
    
#     for sentence in sentences:
#         words = word_tokenize(sentence)
#         try:
#             tagged_words = pos_tag(words)
#             for word, tag in tagged_words:
#                 if tag.startswith('NN'):
#                     nouns.append(word)
#                 elif tag.startswith('VB'):
#                     verbs.append(word)
#                 elif tag.startswith('JJ'):
#                     adjectives.append(word)
#             paragraph = f"Extracted text contains {len(sentences)} sentences. " \
#                         f"It discusses topics like {', '.join(set(nouns))} and actions like " \
#                         f"{', '.join(set(verbs))}. It also includes adjectives like " \
#                         f"{', '.join(set(adjectives))}."
#         except Exception as e:
#             paragraph = ""
    
#     return paragraph

# # Extract images from PDF using PyMuPDF
# def extract_images_from_pdf(pdf_path):
#     create_images_directory()  # Create images directory
#     doc = fitz.open(pdf_path)
#     images = []
    
#     for i in range(len(doc)):
#         page = doc.load_page(i)
#         image_list = page.get_images(full=True)
        
#         for img_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#             image_bytes = base_image["image"]
#             image = Image.open(io.BytesIO(image_bytes))
#             images.append(image)
#             # Save to images folder
#             image_path = os.path.join('images', f"Image-{i}-{img_index}.png")
#             image.save(image_path, "PNG")
    
#     print(f"Total images extracted: {len(images)}")
#     return len(images)

# # Main function to extract images and process them
# def process_pdf_and_images(pdf_path):
#     # Step 1: Extract images from PDF
#     pdf_images = extract_images_from_pdf(pdf_path)
    
#     # Step 2: Process each image
#     for i in range(pdf_images):
#         try:
#             # Load image from images folder
#             image_path = os.path.join('images', f'Image-{i}.png')
#             image = Image.open(image_path)
#             # Step 3: Predict the caption
#             caption = predict_step([image])
#             # Step 4: Extract text from the image using OCR
#             extracted_text = extract_text_from_image(image)
#             # Step 5: Analyze extracted text
#             analysis = analyze_text(extracted_text)

#             # Display or return results
#             print(f"Image {i}: Caption: {caption[0]}")
#             print(f"Image {i}: OCR Analysis: {analysis}")
#         except Exception as e:
#             print(f"Error processing image {i}: {e}")

# # Initialize the captioning model and tokenizer
# model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# max_length = 16
# num_beams = 4
# gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

# # Example usage
# process_pdf_and_images("Edge_ML_Technique_for_Smart_Traffic_Management_in_Intelligent_Transportation_Systems.pdf")

import fitz
from PIL import Image
import pytesseract
import torch
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import numpy as np
import re
import io
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
import logging

class PDFImageProcessor:
    def __init__(self):
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Initialize device and models
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning").to(self.device)
        self.feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        
        # Configure generation parameters
        self.gen_kwargs = {"max_length": 16, "num_beams": 4}
        
        # Set up image directory
        self.image_folder = os.path.join(os.getcwd(), "images")
        self._create_images_directory()

    def _create_images_directory(self):
        """Creates the images directory if it doesn't exist."""
        try:
            if not os.path.exists(self.image_folder):
                os.makedirs(self.image_folder)
                self.logger.info("Created 'images' directory")
        except Exception as e:
            self.logger.error(f"Error creating images directory: {str(e)}")
            raise

    def clean_image_directory(self):
        """Cleans up existing images in the directory."""
        try:
            for file in os.listdir(self.image_folder):
                file_path = os.path.join(self.image_folder, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            self.logger.info("Cleaned images directory")
        except Exception as e:
            self.logger.error(f"Error cleaning images directory: {str(e)}")

    def predict_caption(self, images):
        """Generates captions for images using the vision model."""
        try:
            processed_images = [img.resize((224, 224)) for img in images]
            pixel_values = self.feature_extractor(images=processed_images, return_tensors="pt").pixel_values.to(self.device)
            output_ids = self.model.generate(pixel_values, **self.gen_kwargs)
            return [pred.strip() for pred in self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)]
        except Exception as e:
            self.logger.error(f"Error predicting caption: {str(e)}")
            return ["Error generating caption"]

    def extract_text_from_image(self, image):
        """Extracts text from image using OCR."""
        try:
            extracted_text = pytesseract.image_to_string(image)
            return re.sub(r'[^\w\s]', '', re.sub(r'\d+', '', extracted_text))
        except Exception as e:
            self.logger.error(f"Error extracting text from image: {str(e)}")
            return ""

    def extract_images_from_pdf(self, pdf_path):
        """Extracts images from PDF and saves them to the images directory."""
        try:
            # Clean existing images
            self.clean_image_directory()
            
            doc = fitz.open(pdf_path)
            images = []
            
            for page_num in range(len(doc)):
                for img_index, img in enumerate(doc.load_page(page_num).get_images(full=True)):
                    try:
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image = Image.open(io.BytesIO(base_image["image"]))
                        
                        # Save with consistent naming
                        image_path = os.path.join(self.image_folder, f"image_{page_num}_{img_index}.png")
                        image.save(image_path, "PNG")
                        images.append(image)
                        
                        self.logger.info(f"Extracted and saved image: {image_path}")
                    except Exception as e:
                        self.logger.error(f"Error processing image {img_index} on page {page_num}: {str(e)}")
                        continue
            
            return images
        except Exception as e:
            self.logger.error(f"Error extracting images from PDF: {str(e)}")
            return []

    def process_pdf(self, pdf_path):
        """Main method to process PDF and extract/analyze images."""
        try:
            images = self.extract_images_from_pdf(pdf_path)
            self.logger.info(f"Successfully extracted {len(images)} images from PDF")
            return len(images)
        except Exception as e:
            self.logger.error(f"Error processing PDF: {str(e)}")
            return 0