import argparse
import pandas as pd
from agents import InsightGenerationAgent, DataAugmentationAgent
from utils import load_csv, save_csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--query", required=True, help="User query")
    parser.add_argument(
        "--mode", required=True, choices=["insight", "augment"], help="Agent mode"
    )
    args = parser.parse_args()

    df = load_csv(args.input)

    if args.mode == "insight":
        agent = InsightGenerationAgent()
        result, sql = agent.run(df, args.query)
        print("Generated SQL:", sql)
        print(result)
        if result is not None:
            save_csv(result, "insight_output.csv")

    elif args.mode == "augment":
        agent = DataAugmentationAgent()
        result = agent.run(df,args.query)
        print("Augmented response:", result)

        # If it's structured data, wrap in DataFrame before saving
        try:
            df_aug = pd.DataFrame([{"response": result}])
            save_csv(df_aug, "augment_output.csv")
        except Exception:
            pass


if __name__ == "__main__":
    main()