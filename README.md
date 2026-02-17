Markdown
# 🧾 AI Finance Agent (Milestone 1: Core Logic)

An intelligent multi-modal financial agent powered by **Google Gemini 1.5 Flash**. This agent automates the extraction of invoice data and ensures 100% calculation accuracy by bridging the gap between LLM reasoning and local Python execution.

---

## 🌟 Key Features

- **Multi-modal Perception**: Directly processes invoice images (JPG/PNG) to identify financial fields.
- **Function Calling (Tool Use)**: Eliminates "LLM Hallucinations" in math by offloading tax and total calculations to a verified local Python function.
- **Structured Data Output**: Guarantees a JSON-formatted response, making it ready for integration with accounting software or databases.
- **Security First**: Implements environment variable management to protect sensitive API credentials.

## 🛠️ Tech Stack

- **Language**: Python 3.12+
- **AI Model**: Google Gemini 1.5 Flash (via `google-generativeai`)
- **Image Processing**: Pillow (PIL)
- **Configuration**: Python-dotenv

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone [https://github.com/YourUsername/gemini-agent-demo.git](https://github.com/YourUsername/gemini-agent-demo.git)
cd gemini-agent-demo
pip install -U google-generativeai pillow python-dotenv
2. Configuration
Create a .env file in the root directory and add your API key:

code
GEMINI_API_KEY=your_actual_api_key_here
3. Usage
Place your invoice image in the external/ folder and run:

Bash
python3 agent_with_tools.py
🧠 System Architecture
Input: User provides an invoice image.

Recognition: Gemini identifies the net_amount and tax_rate.

Execution: The agent triggers calculate_tax_and_total locally.

Validation: Python performs precise floating-point math.

Output: The agent compiles the results into a final, structured JSON object.

📈 Roadmap
[x] Milestone 1: Core logic, Function Calling, and JSON output.

[ ] Milestone 2: Interactive Web UI using Streamlit.

[ ] Milestone 3: Automated Export to Excel/CSV for bookkeeping.

Developed as a proof-of-concept for AI-driven financial automation.


---

### 🚀 Push guidence

1. **save file**：make sure`README.md` saved。
2. **terminal command**：
   ```bash
   git add README.md
   git commit -m "docs: update README with professional English version"
   git push origin main