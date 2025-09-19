import pandas as pd
import duckdb

def load_csv(path: str) -> pd.DataFrame:
    """Load CSV into pandas DataFrame."""
    return pd.read_csv(path)

def run_sql(df: pd.DataFrame, sql: str) -> pd.DataFrame:
    """Run SQL on pandas DataFrame using duckdb."""
    duckdb.register("df", df)

    if not sql.strip():
        print("[ERROR] Empty SQL received.")
        return pd.DataFrame()

    try:
        result = duckdb.sql(sql).to_df()
        return result
    except Exception as e:
        print(f"[ERROR] Failed to run SQL: {sql}\nReason: {e}")
        return pd.DataFrame()

def save_csv(df: pd.DataFrame, path: str):
    """Save dataframe as CSV."""
    df.to_csv(path, index=False)