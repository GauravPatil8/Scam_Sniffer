# Scam_Sniffer

This project uses machine learning to detect **fake job postings** on LinkedIn-like platforms. It processes job post data, trains a classifier, and evaluates its performance using real-world-inspired samples.

---
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linkedin_fake_job_post_detector.git
cd linkedin_fake_job_post_detector
```
### 2.Create Virtual Environment
```bash
python -m venv venv
venv/bin/activate  
```

### 3.Install Dependencies
```bash
pip install -r requirements.txt
```

# 🚀 How to Run

## Step 1: Run the Pipeline

```bash
python run.py
```

This will:
- Download the dataset
- Transform and clean the data
- Train a model
- Evaluate its performance

# 🧠 Model Info

Currently supported:
- ✅ XGBoost Classifier
- ✅ Performance metrics: Accuracy, F1, Confusion Matrix

# 📊 Evaluation Example

Sample output:

```yaml
Accuracy: 0.94
Precision: 0.91
Recall: 0.90
F1 Score: 0.905
```

# 📦 Output

After training, outputs are saved in:
- `artifacts/data_transformation/`: Transformed datasets
- `artifacts/model_trainer/xgboost_job_classifier.pkl`: Trained model

# 🛠️ Future Improvements

- Use graph neural networks to detect bot-generated job patterns.
- Chrome extension to verify jobs in real-time.
- Add support for fake recruiter detection.

# 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.



