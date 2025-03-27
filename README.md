# 📄 Paper2PPT

## 🛠️ Overview
This project automates the creation of PowerPoint presentations from research papers using Artificial Intelligence (AI). It extracts key sections, summarizes critical points, and presents them in a structured, visually appealing format. Additionally, it identifies and extracts 📊 **images and charts** from the research paper to include them in the slides. The tool also offers flexibility in presentation styles, allowing users to generate **formal** or **informal** presentations based on their needs. This is particularly beneficial for researchers, educators, and professionals who need to prepare presentations quickly and efficiently.

## 🏆 Hackathon Contribution
This project originated as part of **🏅 Mined Hackathon 2025** organized by **Nirma University**. During the 48-hour hackathon, our team collaborated to design and prototype this innovative solution for a challenge provided by **Cactus Communications**.

## ✨ Features
- 📜 **Text Extraction**: Processes research papers in various formats (PDF, DOCX, etc.).
- 📝 **Content Summarization**: Summarizes abstracts, introductions, methodologies, results, and conclusions.
- 🖼️ **Image Extraction**: Identifies and extracts relevant images, charts, and figures from the research paper for visual enhancement.
- 📑 **Slide Generation**: Converts summarized content and extracted images into PowerPoint slides with proper formatting and structure.
- 🎭 **Presentation Styles**: Supports generating **formal** presentations (e.g., for academic or professional use) and **informal** presentations (e.g., for casual discussions or internal reviews).
- ⚙️ **Customization Options**: Allows users to choose sections to include, adjust slide design, and edit content manually.

## 🖥️ Technology Stack
- **Programming Language**: 🐍 Python
- **Libraries Used**:
  - 📂 `PyPDF2` / `pdfplumber`: For PDF text extraction
  - 📖 `NLTK` / `spaCy`: For natural language processing
  - 🤖 `transformers`: For summarization models (e.g., BART, T5)
  - 📊 `python-pptx`: For creating PowerPoint slides
  - 🖼️ `opencv` / `Pillow`: For image extraction and processing
- **Machine Learning Models**: Pre-trained NLP models for text summarization and keyword extraction.

## ⚙️ How It Works
1. **📂 Input**: Upload a research paper in PDF format.
2. **⚡ Processing**:
   - Extract text and images from the document.
   - Identify key sections using NLP.
   - Summarize each section and extract key phrases.
3. **🎨 Output**: Generate a PowerPoint presentation with:
   - Title and introduction slides.
   - Slides for each major section (e.g., Methods, Results, Conclusion).
   - Visual elements (images, charts, or tables) extracted from the research paper.
   - 🎭 **Formal or Informal Style**: Users can choose between formal (structured and polished) or informal (more relaxed and conversational) slide designs.
4. **✏️ Customization**: Users can modify generated slides before saving.

## 🚧 Challenges and Improvements
- **🚨 Challenges**:
  - Accurate extraction of relevant text from complex research paper layouts.
  - Ensuring that generated summaries capture the core ideas effectively.
  - Extracting high-quality images without artifacts.
- **🚀 Future Improvements**:
  - Enhance summarization with domain-specific training.
  - Improve the design of generated slides for better aesthetics.

## Demo Video of the project
https://github.com/user-attachments/assets/8c495dd9-5570-428d-afa9-7b819e32b666

## 🔧 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/research-paper-to-ppt.git
Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py

📝 Usage
📤 Upload a research paper in the supported format.

🛠️ Select the sections you want to include.

🎭 Choose the presentation style: Formal or Informal.

🖋️ Review and customize the generated slides.

💾 Save or export the final presentation.

🤝 Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

📧 Contact
This version highlights the dual capability of generating both formal and informal presentations.
