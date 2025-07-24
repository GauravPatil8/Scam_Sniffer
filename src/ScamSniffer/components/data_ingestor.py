import os
import tqdm
import shutil 
import kagglehub
import mlcroissant as mlc
from ScamSniffer.utils.stages import Stages
from ScamSniffer.utils.common import read_yaml
from ScamSniffer.constants.common import CONFIG_PATH, PROJECT_ROOT
from ScamSniffer.components.data_simulation import generate_dataset

class DataIngestor(Stages):
    """
        Downloads, creates and stores datasets required for training the model.
    """
    def __init__(self):
        self.config = read_yaml(CONFIG_PATH)
        self.kaggel_dataset_path = self.config.data_ingestion.kaggle_dataset_link
        self.output_dir = self.config.data_ingestion.root_dir
        self.simulated_dataset_path = self.config.data_ingestion.simulated_dataset
        print("dataindestor stage init")
        print(self.kaggel_dataset_path)

    def run(self):
        os.makedirs(self.output_dir, exist_ok=True)

        # Download dataset from kaggle
        try: 
            dir_path = kagglehub.dataset_download("shivamb/real-or-fake-fake-jobposting-prediction")
            
            # Moving the files from temp storage to artifacts folder 
            for file in os.listdir(dir_path):
                print(os.path.join(dir_path, file))
                print(os.path.join(self.output_dir,file))
                
                shutil.move(os.path.join(dir_path, file), os.path.join(self.output_dir,file))
        except Exception as e:
            print("Error occured while downloading.", e)


        #Simulating fraud LinkedIn job post data
        generate_dataset(self.simulated_dataset_path, 1000)
