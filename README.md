# 🏥 MedAI - Vision and Voice Medical Assistant

MedAI is an AI-driven healthcare assistant that combines computer vision and natural language processing to provide smart medical consultations through images and voice.

---

## 🚀 Features

- **Image Understanding**  
  Integrated **Meta Llama3 Vision 90B** to analyze and interpret medical images.  

- **Accurate Voice Transcription**  
  Used **OpenAI Whisper** for high-quality speech-to-text conversion.  

- **Advanced Text-to-Speech**  
  Implemented **gTTS** and **ElevenLabs** for natural and interactive doctor-patient voice communication.  

- **Interactive Gradio Interface**  
  A simple, user-friendly **Gradio app** for smooth medical consultations.  

---

# 📂 Project Structure

- `acne.jpg` → Sample medical image  
- `brain_doc.py` → Brain diagnosis module  
- `gradio_app.py` → Main Gradio application  
- `voice_doctor.py` → AI doctor voice interaction logic  
- `voice_patient.py` → Patient voice interface logic  
- `README.md` → Project documentation  

---

# ⚙️ Installation & Usage

- Clone the repository  
- git clone https://github.com/havilah-12/MedAI.git
- cd MedAI

## Install dependencies

- pip install -r requirements.txt
- Run the Gradio app

- python gradio_app.py
- Access the web interface
- Default URL: http://127.0.0.1:7860/

# 🛠 Tech Stack
- Python

- Meta Llama3 Vision 90B → For medical image understanding

- OpenAI Whisper → For accurate speech-to-text conversion

- gTTS & ElevenLabs → For dynamic, natural text-to-speech responses

- Gradio → For an interactive, user-friendly interface

