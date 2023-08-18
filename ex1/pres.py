######## Data Processing ########
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer

# read data from csv file and convert to dataset
dat = pd.read_csv('dat.csv')
dat = Dataset.from_pandas(dat)

# Defining the tokenizer and tokenizing the text
model_ckpt = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
batch_tokenize = lambda batch: tokenizer(
    batch['text'], padding="max_length", truncation=True
)
dat = dat.map(batch_tokenize, batched=True)


######## Feature Extraction ########
import torch
torch.manual_seed(0) # for reproducibility
from transformers import AutoModel

# Convert the dataset to PyTorch tensors
dat.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])

# Loading the model and moving it to the GPU if available
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# Loading distilbert-base-uncased and moving it to the GPU if available
model = AutoModel.from_pretrained(model_ckpt).to(device)


def extract_features(batch):
    # Each batch is a dictionary with keys corresponding to the feature names.
    inputs = {k:v.to(device) for k, v in batch.items() if k in tokenizer.model_input_names}

    # Tell torch not to build the computation graph during inference with `torch.no_grad()`
    with torch.no_grad():
        last_hidden_state = model(**inputs).last_hidden_state # Extract last hidden states

    # Return vector for [CLS] token
    return {"hidden_state": last_hidden_state[:,0].cpu().numpy()}


# Extracting features
dat = dat.map(extract_features, batched=True, batch_size=8)


######## Using features in regression task ########
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split

# Converting features to a pandas dataframe for compatibility with sklearn
embeds = pd.DataFrame(dat['hidden_state'])

# Instantiating the RidgeCV model
regr = RidgeCV()

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(embeds, dat['labels'], random_state=42)

# Fitting the model and evaluating performance
regr.fit(X_train, y_train)
print(f'Test R2 = {regr.score(X_test, y_test).round(2)}')


######## Finetuning ########



