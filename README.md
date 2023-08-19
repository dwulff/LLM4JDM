## Large language models in jugdment and decision making research
### A workshop by Zak Hussain, Sudeep Bhatia, and Dirk Wulff
<br>

### Location & Time
<b>Meeting room</b>: LC.2.400 Club lounge (see [google maps](https://goo.gl/maps/9NQky6m7Dx6pUQ5V6))<br> 
<b>Venue</b>: Vienna University of Economics and Business (Wirtschaftsuniversität Wien, WU)<br> 
<b>Address</b>: Welthandelsplatz 1, 1020 Vienna |Building: Library and Learning Center (LC)<br> 
<b>Time</b>: August 20th, between 9:45 AM - 3:00 PM

### Schedule
9:45 AM - 10:15 AM: [Intro to large language models](LLM4JDM_Intro.pdf)<br>
10:15 AM - 10:45 AM: Intro to Huggingface<br>
10:45 AM - 11:15 AM: Break<br>
11:15 AM - 12:00 PM: Exercise 1 - Predicting health perception<br>
12:00 PM - 1:00 PM: Lunch<br>
1:00 PM - 2:00 PM: Exercise 2 - Predicting personality structure<br>
2:00 PM - 2:30 PM: Exercise 3 - Predicting cognitive reflection<br>
2:30 PM - 3:00 PM: Discussion<br>

### Resources
[Hugging face documentation](https://huggingface.co/docs)<br>
[Hugging face book](https://transformersbook.com/)

### Environment Setup
There are two options for setting up your Python environment: (i) Google Colab (cloud-based), (ii) Locally. For the
purposes of this workshop, we recommend using Golab due to the ease of setup and the availability of GPUs. However, if
you would like to use your own machine, we also provide instructions for setting up your environment locally.

#### (i) Google Colab
1. If you do not have a Google account, you will need to create one (this can be deleted after the workshop).
2. Navigate to Google Drive (https://drive.google.com/).
3. In the top-left, click New > More > Colaboratory. If you do not see Colaboratory, you may need to click "Connect more apps", 
search for 'Colaboratory', and install it. Then click New > More > Colaboratory.

************
Please only do the following on the day of the workshop
***********

5. Run the following code snipped in the first cell (```shift + enter```) of your notebook to mount your Google Drive to the Colab environment.
A pop-up will ask you to connect, click through the steps to connect your Google Drive to Colab (you will have to do this
every time you open a new notebook).
```
from google.colab import drive
drive.mount("/content/drive")
```
5. Clone the GitHub repository to your Google Drive by running the following code snippet in the second cell of your notebook:
```
%cd /content/drive/MyDrive
!git clone https://github.com/dwulff/LLM4JDM.git
```
6. Go back to your Google Drive and navigate to the folder "LLM4JDM". You should see the directories ex1, ex2, and ex3 
containing the relevant notebooks (.ipynb files) and data (it may take  a couple of minutes for the files to appear).
7. Open the notebook for exercise 1 (vaccine.ipynb)
8. In the top-menu bar, click Runtime > Change runtime type > Hardware accelerator > T4 GPU
9. Run the first cell of the notebook to install the required packages. This may take a few minutes and ask for you to
give permission to access your Google Drive. 
You are now ready to start the exercises!

#### (ii) Local
1. Install miniconda  (https://docs.conda.io/en/latest/miniconda.html)
2. Create a new conda environment by running the following command in your terminal:
```
conda create --name LLM4JDM python=3.8
```
The terminal will ask you to confirm the installation. Type "y" and press enter (do the same for any subsequent steps).
3. Activate the environment by running the following command in your terminal:
```
conda activate LLM4JDM
```
4. Install the required packages by running the following commands in your terminal:
```
conda install -c huggingface -c conda-forge jupyter pandas numpy scikit-learn transformers datasets accelerate
```
and
```
pip install evaluate
```
5. Install PyTorch. If you are using a Mac, you can install an Apple M1/M2 GPU compatible version of PyTorch by running the 
following command in your terminal (this will drastically speed up the exercises if your Mac has an M1/M2 chip):
```
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
```
If you are using Windows or Linux, please follow the instructions at https://pytorch.org/get-started/locally/ to install
the appropriate version of PyTorch for your system.

************
Please only do the following on the day of the workshop
***********

6. Download the GitHub repository from https://github.com/dwulff/LLM4JDM and unzip it.
7. Navigate to the folder "LLM4JDM" in your terminal.
8. Run the following command in your terminal to start the Jupyter notebook server:
```
jupyter notebook
```
You are now ready to start the exercises!




