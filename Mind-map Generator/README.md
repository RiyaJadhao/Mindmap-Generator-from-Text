# Mind Map Generator from Text

A simple and effective Python-based application that generates a **visual mind map** from any input text using **Natural Language Processing (spaCy)** and **graph visualization (NetworkX + Matplotlib)**.  
Built with a user-friendly **Tkinter GUI**, the tool helps visualize core concepts and their relationships in a clean, node-based mind map format.

---

## Features

- Input any block of English text
- Automatically extracts **keywords** and **noun phrases**
- Visualizes them in a **mind map format**
- Colorful, interactive display using NetworkX & Matplotlib
- Export the mind map as a high-resolution image
- 100% offline, Python-only solution

---

## Technologies Used

- `Python 3.x`
- `Tkinter` – GUI interface
- `spaCy` – for keyword/noun phrase extraction
- `NetworkX` – graph-based data structure
- `Matplotlib` – to visualize the mind map

---

## How It Works

1. User enters a **title** and **text content**
2. The app uses `spaCy` to identify key noun phrases
3. A central node is created from the title
4. All keyword nodes are connected to the central node
5. The graph is visualized using NetworkX's spring layout
6. User can optionally **export the graph as PNG**

---

## Installation


### 1. Clone this repository
```bash
git clone https://github.com/RiyaJadhao/Mindmap-Generator-from-Text.git

# Navigate to the folder
cd mindmap-generator

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required packages
pip install -r requirements.txt

# Download spaCy English model
python -m spacy download en_core_web_sm

# Run the Application
python main.py

