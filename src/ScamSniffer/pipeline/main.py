import tqdm
import asyncio
import os
from ScamSniffer.utils.stages import Stages
from ScamSniffer.components.data_ingestor import DataIngestor
from ScamSniffer.components.data_transformer import DataTransformer
from ScamSniffer.components.model_trainer import ModelTrainer
from ScamSniffer.components.model_evaluator import ModelEvaluator

class Pipeline:
    def __init__(self):
        print("pipline init")
        self.stages = [DataIngestor, DataTransformer, ModelTrainer, ModelEvaluator]

    def run(self):
        for stage in tqdm.tqdm(self.stages, desc="Running Pipeline"):
            model_stage = stage()
            model_stage.run()
