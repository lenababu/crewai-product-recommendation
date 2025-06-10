# 🧠 CrewAI Product Recommendation System

This project uses **CrewAI** with **LLMs** to build an intelligent **AI-powered product recommendation system**. It automates product research, feature analysis, and personalized recommendations using a team of specialized agents.

---

## 🚀 Features

- 🔍 **Automated Research Agents**: Each agent has a specific role (researcher, analyst, recommender).
- 📊 **Structured Reports**: Outputs include research findings, comparisons, and final recommendations.
- 🧩 **Modular Architecture**: Cleanly separated into `config`, `tools`, and `src` for easy customization.
- 🗂️ **Markdown Exports**: Results are saved to `report.md`, `research.md`, and `recommendation.md`.

---

## 🏗️ Project Structure

```

latest\_ai\_development/
│
├── .env.example                # Sample environment config
├── crew\.py                    # CrewAI agent definitions and roles
├── main.py                    # Entry point to run the Crew
├── config/                    # Configuration files
├── tools/                     # Utility functions and tools
├── tests/                     # Test scripts (optional)
├── report.md                  # Summary report generated
├── research.md                # In-depth research findings
├── recommendation.md          # Final product recommendations
└── README.md                  # Project overview and instructions

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/lenababu/crewai-product-recommendation.git
cd crewai-product-recommendation
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or if using `pyproject.toml`:

```bash
pip install .
```

### 4. Add your environment variables

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp latest_ai_development/.env.example latest_ai_development/.env
```

---

## 🧠 How It Works

1. Agents are defined in `crew.py` (e.g., Product Researcher, Analyst).
2. Running `main.py` starts the crew and executes the workflow.
3. Final output is saved as markdown reports with insights and recommendations.

---

## 📦 Run the Crew

```bash
python src/latest_ai_development/main.py run
```

---

## 🧪 Example Use Case

> **Find the best cars under ₹10 lakhs**
> The Crew will research options, compare features, evaluate user reviews, and produce a final recommendation report.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* [CrewAI](https://docs.crewai.com/)
* [Groq LLaMA 3](https://groq.com/)
  

Made by Lena Babu❤️

