# llm-sql-augmentor
An **LLM-powered agent system** that works with structured datasets (CSV, XLSX) to provide:

1. **Insight Generation** → Convert natural language queries into SQL (DuckDB) and return insights.  
2. **Data Augmentation** → Enhance datasets by applying annotations or transformations suggested by an LLM.

Built with **Python**, **DuckDB**, and **OpenRouter API** (supports DeepSeek, Llama, etc.).

---

##  Features
-  Natural language → SQL query generation
-  Execute queries on CSV data via DuckDB
-  Augment datasets with new fields
-  Save outputs as CSV
-  Secure API key management via `.env`

---

## Project Structure

```
llama_endpoint/
│── agents.py              # InsightGenerationAgent & DataAugmentationAgent
│── utils.py               # Helpers (CSV load/save, SQL runner)
│── main.py                # CLI entry point
│── sample_glassdoor.csv   # Example dataset
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

##  Installation

Clone this repo and set up your environment:

```bash
git clone https://github.com/https://github.com/rc02041998/llm-sql-augmentor
cd llm-sql-augmentor
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Environment Setup

Create a `.env` file in the project root:

```
OPENROUTER_API=your_openrouter_api_key
MODEL=deepseek-chat
```

---

##  Usage

### 1. Insight Generation
Convert natural language to SQL and run it on your CSV:

```bash
python main.py --input sample_glassdoor.csv \
               --query "Show the count of reviews of each designation" \
               --mode insight
```

 Outputs:  
- Generated SQL query  
- Results printed in terminal  
- Saved as `insight_output.csv`

---

### 2. Data Augmentation
Add new annotations/fields to the dataset:

```bash
python main.py --input sample_glassdoor.csv \
               --query "Add a column 'sentiment' labeling each review as 'positive' (rating >=4), 'neutral' (rating 3), or 'negative' (rating <=2)." \
               --mode augment
```

 Outputs:  
- Augmented dataset  
- Saved as `augment_output.csv`

---

## Example Dataset

**`sample_glassdoor.csv`**

| designation  | rating | review_text                               | date       |
|--------------|--------|-------------------------------------------|------------|
| Software Eng | 5      | Great place to work                      | 2018-08-01 |
| Analyst      | 2      | Poor management and long hours           | 2018-08-05 |
| Manager      | 3      | Average experience                       | 2018-08-12 |
| Intern       | 1      | Toxic culture, no learning opportunities | 2018-08-15 |

---

##  Requirements
- Python 3.9+  
- Pandas  
- DuckDB  
- OpenAI Python client  
- python-dotenv  

Install all with:

```bash
pip install -r requirements.txt
```

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## Acknowledgements
- [DuckDB](https://duckdb.org/) for in-memory SQL execution  
- [OpenRouter](https://openrouter.ai/) for LLM access  
- [Pandas](https://pandas.pydata.org/) for data handling  
