# 🧠 Infooware Edu Prototype — PDF to Slides & Short Video

This project converts an **input PDF chapter/article** into:
- A **slide deck** (`slides.pptx`) with visuals and concise summaries.
- A **short explainer video** (`video.mp4`) with **text-to-speech narration**, icons, and background music.

---

## 🎯 Project Goal
To automatically summarize and visualize educational documents into short multimedia explainers.

---

## 🧩 Features
✅ PDF text extraction  
✅ Section-based summarization  
✅ Auto-generated PowerPoint slides  
✅ Icon & visual integration  
✅ Text-to-speech narration (offline pyttsx3)  
✅ Dynamic slide duration and fade transitions  
✅ Background music blending  

---

## ⚙️ Tech Stack
**Language:** Python  
**Libraries:** `pdfplumber`, `python-pptx`, `Pillow`, `moviepy`, `pyttsx3`, `nltk`, `scikit-learn`

---

## 🚀 How to Run

### 1️⃣ Setup Environment
```bash
git clone https://github.com/<your-username>/infooware-edu-prototype.git
cd infooware-edu-prototype
pip install -r requirements.txt


2️⃣ Run the pipeline
python src/run_pipeline.py --input sample_inputs/sample.pdf --outdir output/

3️⃣ Outputs
output/slides.pptx   → 6–12 summarized slides
output/video.mp4     → 30–90 sec video with narration

🧠 Example Output
File	            Description
slides.pptx	      Auto-generated deck with title, summary, and icons per slide
video.mp4	        Narrated video version with fade transitions and background music
