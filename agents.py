import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from utils import run_sql

# Load environment variables
load_dotenv()
OPENROUTER_API = os.getenv("OPENROUTER_API")
model = os.getenv("MODEL")


class InsightGenerationAgent:
    """Agent for SQL-based insight generation."""

    def __init__(self, model=model):  # keep model consistent
        self.model = model
        self.client = OpenAI(
            api_key=OPENROUTER_API,
            base_url="https://openrouter.ai/api/v1"
        )

    def run(self, df, query: str):
        prompt = f"""
        You are a data analyst. Convert the user query into a valid SQL query for DuckDB.
        Query: {query}
        Table: df
        Only output SQL, no explanations, no markdown.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        sql = response.choices[0].message.content.strip()

        # ✅ Clean SQL if wrapped in markdown fences
        sql = sql.replace("```sql", "").replace("```", "").strip()

        try:
            result_df = run_sql(df, sql)
        except Exception as e:
            print("[ERROR] Failed to run SQL:\nReason:", str(e))
            print("Generated SQL:", sql)
            return None, sql

        return result_df, sql


class DataAugmentationAgent:
    """Agent for augmenting/querying structured datasets."""

    def __init__(self, model=model):  # keep model consistent
        self.model = model
        self.client = OpenAI(
            api_key=OPENROUTER_API,
            base_url="https://openrouter.ai/api/v1"
        )

    def run(self, df, query: str):
        prompt = f"""
        You are a data augmentation assistant. 
        Given the dataframe rows and a user query, return an augmented dataframe in JSON format only. 
        - Each row must include all original fields plus the new/modified fields requested. 
        - Do not include explanations, only JSON array output.

        Query: {query}
        Data sample (first 5 rows): {df.to_dict(orient="records")}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content.strip()

        # ✅ Clean markdown fences if present
        content = content.replace("```json", "").replace("```", "").strip()

        try:
            augmented_rows = json.loads(content)
            return pd.DataFrame(augmented_rows)
        except Exception as e:
            print("[ERROR] Failed to parse augmentation JSON:", str(e))
            print("Raw response:", content)
            return df