# import streamlit as st
# import base64
# import os
# from pptgenerate import PDFtoPPTGenerator
# from imagefoldergen import PDFImageProcessor
# from append import append_images_to_ppt
# from beststyling import PPTStyleApplicator

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(125deg, #0a0a14 0%, #1a1a3a 100%);
#         color: #ffffff;
#     }
    
#     .custom-card {
#         background: rgba(255, 255, 255, 0.05);  
#         border-left: 4px solid rgba(255, 105, 180, 0.5);
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         backdrop-filter: blur(5px);
#     }
    
#     h1 {
#         background: linear-gradient(45deg, #ff69b4, #00bfff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 2.5em !important;
#         text-align: center;
#     }
    
#     .option-container {
#         display: flex;
#         justify-content: center;
#         gap: 20px;
#         margin-top: 20px;
#         margin-bottom: 30px;
#     }
    
#     .option-box {
#         width: 180px;
#         padding: 15px;
#         text-align: center;
#         font-size: 1.2rem;
#         font-weight: bold;
#         border-radius: 10px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         border: 2px solid transparent;
#         background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(5px);
#     }
    
#     .selected {
#         border-color: #ff69b4;
#         box-shadow: 0 0 20px rgba(255, 105, 180, 0.7);
#     }
    
#     .stButton > button {
#         background: rgba(255, 255, 255, 0.05) !important;
#         border: 1px solid rgba(255, 255, 255, 0.1) !important;
#         color: white !important;
#         padding: 0.75rem 2rem !important;
#         border-radius: 10px !important;
#         font-size: 1.2rem !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 0 15px rgba(255, 105, 180, 0.2) !important;
#         margin-top: 20px !important;
#         width: 100% !important;
#     }
    
#     .stButton > button:hover {
#         background: rgba(255, 255, 255, 0.1) !important;
#         transform: translateY(-2px) !important;
#         box-shadow: 0 0 25px rgba(0, 191, 255, 0.3) !important;
#     }
    
#     .custom-warning {
#         background: rgba(255, 69, 58, 0.2);
#         border-left: 4px solid rgba(255, 69, 58, 0.7);
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         backdrop-filter: blur(5px);
#         color: #ff453a;
#         font-weight: bold;
#         text-align: center;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <div class="custom-card">
#         <h1>Research Paper to PPT Converter</h1>
#     </div>
# """, unsafe_allow_html=True)

# def process_pdf(uploaded_file, style_option):
#     try:
#         # Save uploaded file temporarily
#         temp_pdf_path = "temp_uploaded.pdf"
#         with open(temp_pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
        
#         # Step 1: Generate initial PPT
#         ppt_generator = PDFtoPPTGenerator()
#         output_ppt = "temp_presentation.pptx"
#         ppt_generator.process(temp_pdf_path, output_ppt)
        
#         # Step 2: Process images
#         image_processor = PDFImageProcessor()
#         image_processor.process_pdf(temp_pdf_path)
        
#         # Step 3: Append images to PPT
#         append_images_to_ppt(output_ppt, "images")
        
#         # Step 4: Apply styling
#         style_applicator = PPTStyleApplicator()
#         final_ppt = "final_presentation.pptx"
#         style_applicator.apply_styling(output_ppt, final_ppt)
        
#         # Clean up temporary files
#         if os.path.exists(temp_pdf_path):
#             os.remove(temp_pdf_path)
#         if os.path.exists(output_ppt):
#             os.remove(output_ppt)
            
#         return final_ppt
        
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")
#         return None

# # File uploader
# uploaded_file = st.file_uploader("Upload your PDF", type=['pdf'])

# if uploaded_file is not None:
#     # Selection layout
#     st.markdown('<div class="option-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)

#     with col1:
#         formal = st.button("Formal")
#     with col2:
#         creative = st.button("Creative")
    
#     st.markdown('</div>', unsafe_allow_html=True)

#     if formal or creative:
#         style_option = "formal" if formal else "creative"
        
#         with st.spinner("Processing your PDF..."):
#             final_ppt = process_pdf(uploaded_file, style_option)
            
#             if final_ppt and os.path.exists(final_ppt):
#                 with open(final_ppt, "rb") as file:
#                     btn = st.download_button(
#                         label="Download Presentation",
#                         data=file,
#                         file_name="research_presentation.pptx",
#                         mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#                     )
#                 # Clean up final presentation after download
#                 if os.path.exists(final_ppt):
#                     os.remove(final_ppt)

# else:
#     st.markdown("<div class='custom-warning'>⚠️ Please upload a PDF to begin.</div>", unsafe_allow_html=True)

# import streamlit as st
# import os
# from pptgenerate import PDFtoPPTGenerator
# from imagefoldergen import PDFImageProcessor
# from append import PPTImageAppender
# from beststyling import PPTStyleApplicator

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(125deg, #0a0a14 0%, #1a1a3a 100%);
#         color: #ffffff;
#     }
    
#     .custom-card {
#         background: rgba(255, 255, 255, 0.05);  
#         border-left: 4px solid rgba(255, 105, 180, 0.5);
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         backdrop-filter: blur(5px);
#     }
    
#     h1 {
#         background: linear-gradient(45deg, #ff69b4, #00bfff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 2.5em !important;
#         text-align: center;
#     }
    
#     .option-container {
#         display: flex;
#         justify-content: center;
#         gap: 20px;
#         margin-top: 20px;
#         margin-bottom: 30px;
#     }
    
#     .option-box {
#         width: 180px;
#         padding: 15px;
#         text-align: center;
#         font-size: 1.2rem;
#         font-weight: bold;
#         border-radius: 10px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         border: 2px solid transparent;
#         background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(5px);
#     }
    
#     .selected {
#         border-color: #ff69b4;
#         box-shadow: 0 0 20px rgba(255, 105, 180, 0.7);
#     }
    
#     .stButton > button {
#         background: rgba(255, 255, 255, 0.05) !important;
#         border: 1px solid rgba(255, 255, 255, 0.1) !important;
#         color: white !important;
#         padding: 0.75rem 2rem !important;
#         border-radius: 10px !important;
#         font-size: 1.2rem !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 0 15px rgba(255, 105, 180, 0.2) !important;
#         margin-top: 20px !important;
#         width: 100% !important;
#     }
    
#     .stButton > button:hover {
#         background: rgba(255, 255, 255, 0.1) !important;
#         transform: translateY(-2px) !important;
#         box-shadow: 0 0 25px rgba(0, 191, 255, 0.3) !important;
#     }
    
#     .custom-warning {
#         background: rgba(255, 69, 58, 0.2);
#         border-left: 4px solid rgba(255, 69, 58, 0.7);
#         padding: 15px;
#         border-radius: 10px;
#         margin: 10px 0;
#         backdrop-filter: blur(5px);
#         color: #ff453a;
#         font-weight: bold;
#         text-align: center;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # App header
# st.markdown("""
#     <div class="custom-card">
#         <h1>Research Paper to PPT Converter</h1>
#     </div>
# """, unsafe_allow_html=True)

# # File uploader
# uploaded_file = st.file_uploader("Upload your PDF", type=['pdf'])

# # Process PDF and generate PPT
# def process_pdf(uploaded_file, style_option):
#     try:
#         # Save uploaded file temporarily
#         temp_pdf_path = "temp_uploaded.pdf"
#         with open(temp_pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
        
#         # Step 1: Generate initial PPT
#         ppt_generator = PDFtoPPTGenerator()
#         output_ppt = "temp_presentation.pptx"
#         ppt_generator.process(temp_pdf_path, output_ppt)

#         # Step 2: Process images
#         image_processor = PDFImageProcessor()
#         image_processor.process_pdf(temp_pdf_path)
        
#         # Step 3: Append images to PPT
#         ppt_image_appender = PPTImageAppender(output_ppt, "images")
#         ppt_image_appender.append_images_and_add_thank_you()

#         # Step 4: Apply styling
#         style_applicator = PPTStyleApplicator()
#         final_ppt = "final_presentation.pptx"
#         style_applicator.apply_styling(output_ppt, final_ppt)
        
#         # Return the final PPT file if created
#         if os.path.exists(final_ppt):
#             return final_ppt
#         else:
#             st.error("Failed to generate the final presentation.")
#             return None
        
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")
#         return None


# if uploaded_file is not None:
#     # Selection layout for style
#     st.markdown('<div class="option-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)

#     with col1:
#         formal = st.button("Formal")
#     with col2:
#         creative = st.button("Creative")
    
#     st.markdown('</div>', unsafe_allow_html=True)

#     if formal :
#         style_option = "formal" if formal else "creative"
        
#         with st.spinner("Processing your PDF..."):
#             final_ppt = process_pdf(uploaded_file, style_option)
            
#             if final_ppt and os.path.exists(final_ppt):
#                 with open(final_ppt, "rb") as file:
#                     st.download_button(
#                         label="Download Presentation",
#                         data=file,
#                         file_name="research_presentation.pptx",
#                         mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#                     )
                
#                 # Clean up the final PPT after download
#                 if os.path.exists(final_ppt):
#                     os.remove(final_ppt)
#     if creative :
#         st.markdown("""
#             HELLO WORLD
#         """, unsafe_allow_html=True)

# else:
#     st.markdown("<div class='custom-warning'>⚠️ Please upload a PDF to begin.</div>", unsafe_allow_html=True)

import streamlit as st
import os
from pptgenerate import PDFtoPPTGenerator
from imagefoldergen import PDFImageProcessor
from append import PPTImageAppender
from beststyling import PPTStyleApplicator

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(125deg, #0a0a14 0%, #1a1a3a 100%);
        color: #ffffff;
    }
    
    .custom-card {
        background: rgba(255, 255, 255, 0.05);  
        border-left: 4px solid rgba(255, 105, 180, 0.5);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        backdrop-filter: blur(5px);
    }
    
    h1 {
        background: linear-gradient(45deg, #ff69b4, #00bfff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5em !important;
        text-align: center;
    }
    
    .option-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    
    .option-box {
        width: 180px;
        padding: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(5px);
    }
    
    .selected {
        border-color: #ff69b4;
        box-shadow: 0 0 20px rgba(255, 105, 180, 0.7);
    }
    
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        border-radius: 10px !important;
        font-size: 1.2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 15px rgba(255, 105, 180, 0.2) !important;
        margin-top: 20px !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 0 25px rgba(0, 191, 255, 0.3) !important;
    }
    
    .custom-warning {
        background: rgba(255, 69, 58, 0.2);
        border-left: 4px solid rgba(255, 69, 58, 0.7);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        backdrop-filter: blur(5px);
        color: #ff453a;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown("""
    <div class="custom-card">
        <h1>Research Paper to PPT Converter</h1>
    </div>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=['pdf'])

# Process PDF and generate PPT
def process_pdf(uploaded_file, style_option):
    try:
        # Save uploaded file dynamically with a unique name
        temp_pdf_path = f"temp_uploaded_{uploaded_file.name}"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Step 1: Generate initial PPT
        ppt_generator = PDFtoPPTGenerator()
        output_ppt = "temp_presentation.pptx"
        ppt_generator.process(temp_pdf_path, output_ppt)

        # Step 2: Process images
        image_processor = PDFImageProcessor()
        image_processor.process_pdf(temp_pdf_path)
        
        # Step 3: Append images to PPT
        ppt_image_appender = PPTImageAppender(output_ppt, "images")
        ppt_image_appender.append_images_and_add_thank_you()

        # Step 4: Apply styling
        style_applicator = PPTStyleApplicator()
        final_ppt = "final_presentation.pptx"
        style_applicator.apply_styling(output_ppt, final_ppt)
        
        # Return the final PPT file if created
        if os.path.exists(final_ppt):
            return final_ppt
        else:
            st.error("Failed to generate the final presentation.")
            return None
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


if uploaded_file is not None:
    # Selection layout for style
    st.markdown('<div class="option-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        formal = st.button("Formal")
    with col2:
        creative = st.button("Creative")
    
    st.markdown('</div>', unsafe_allow_html=True)

    if formal:
        style_option = "formal" if formal else "creative"
        
        with st.spinner("Processing your PDF..."):
            final_ppt = process_pdf(uploaded_file, style_option)
            
            if final_ppt and os.path.exists(final_ppt):
                with open(final_ppt, "rb") as file:
                    st.download_button(
                        label="Download Presentation",
                        data=file,
                        file_name="research_presentation.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                    )
                
                # Clean up the final PPT after download
                if os.path.exists(final_ppt):
                    os.remove(final_ppt)
    if creative:
        st.markdown("""
            HELLO WORLD
        """, unsafe_allow_html=True)

else:
    st.markdown("<div class='custom-warning'>⚠️ Please upload a PDF to begin.</div>", unsafe_allow_html=True)
