import sys

sys.path.insert(0, "src")

from src.ScamSniffer.pipeline.main import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()


