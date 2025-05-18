## 📋 Prerequisites
- Python 3.8+

## 🚀 Installation

1. Clone this repository:
'''
git clone https://github.com/ebidotpy/HadafPlus_task.git
cd HadafPlus_task
'''

2. Create a virtual environment and activate it:
'''
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
'''

3. Install ollama
for ubuntu:
''
curl https://ollama.ai/install.sh | sh
ollama serve &
'''
for windows go to this link:
[ollama.com](https://ollama.com/)

4. Pull modle that you want
for example:
''' 
ollama pull llama3
'''

5. Install the required pckages:
'''
pip install -r requirements.txt
'''

6. Log in on your huggingface acoount with this command (before running command prepare your huggingface token):
''' 
huggingface-cli login
'''
NOTE: If the above command didn't worked make soure you have installed huggingface_hub liberary. for installing it you can use below command:
'''
pip install -U "huggingface_hub[cli]"
'''

## 💻 Usage

1. Start the application with one of this commands:
'''
python main.py
uvicorn api.server:app --host 0.0.0.0 --port 8000 --reload
'''

1. Navigate to this url on your browser:
'''
http://0.0.0.0:8000/docs
'''
