Markdown
# 🧾 AI Finance Agent (Milestone 1)

An intelligent multi-modal financial agent powered by **Google Gemini 1.5 Flash**.

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone [https://github.com/YourUsername/gemini-agent-demo.git](https://github.com/YourUsername/gemini-agent-demo.git)
cd gemini-agent-demo
pip install -U google-generativeai pillow python-dotenv
```

### 2. Configuration
``` bash
Create a .env file in the root directory and add your API key:
GEMINI_API_KEY=your_actual_api_key_here
```

3. Usage
```Bash
python3 agent_with_tools.py
```

🧠 System Architecture
Input: User provides an invoice image.

Recognition: Gemini identifies net_amount and tax_rate.

Execution: Agent triggers calculate_tax_and_total locally.

Output: Compiles results into a final, structured JSON object.

Status: Milestone 1 Completed