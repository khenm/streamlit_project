# Streamlit Project
> Simple implementations built on Streamlit

Streamlit Project is comprised of 3 sub-projects, namely Word Correction, Object Detection, and Chatbot. In which, 
* **Word Correction** uses Levenshtein algorithm to find the minimum number of changes for source to reach the target. The targets are extracted from an existing list of vocabularies and the correct word can be concluded based on the word that has the smallest Levenshtein distance.
* **Object Detection** is a elemental implementation of image processing. In this project, the system requires user's input image and use DNN Model from opencv to create a bounding box for targets. 
* **Chatbot** is overwhemingly popular recently, in which most of them use LLM to interact with user. This project is mainly a simple chatbot based on *hugchat* and streamlit library with an ability to answer basic questions. 


## 1. Clone the repository

```sh
git clone https://github.com/khenm/streamlit_project.git
cd folder-name #cd - change directory to the folder storing cloned git
```

## 2. (Optional) Create and activate a virtual environment
* For Unix/macOS:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

* For Windows:

```sh
python -m venv venv
.\venv\Scripts\activate
```

## 3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Release History
* 0.1.0
    * The first proper release
* 0.0.1
    * Inital commit
    * SonarCloud added