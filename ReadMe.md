## The Project

A bot I made that ran it's own Facebook page. (has since been taken down by Meta as it apparently went against their guidelines) 
Every morning at 9am it would get the top 10 searches from Yahoo. 
It would then Google those searches and grab the top 10 results for each and use them to generate prompts for a GPT2 LLM. 
The model I was using came pre-trained on Plato's 'The Republic'
I then further trained it myself for over 25,000 epochs on the top 10,000 comments from the top 10,000 posts on Reddit.


## Getting Started

pip install -r requirements.txt

update modules with your account token and idn

update automat with the proper file path to your cloned repository

run automat.bat with powershell or use windows task scheduler to have it automatically

### Prerequisites

python and all the required libraries in requirements.txt

### Installing

clone the repo or download the zip file and unzip it in desired location


## Built With

* OpenAI's GPT2 - https://github.com/openai/gpt-2
* Facebook API - https://www.facebook.com/
* Python 3.8


## Authors

* **Frederick Lyle** - *Initial work* - (https://github.com/OdincoGaming)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
