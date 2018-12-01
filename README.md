# census-scraper
## Intallation
1. Install dependencies
 ```bash
 $ sudo apt-get install python3-pip python3-virtualenv git
 ```
2. Clone repo
```bash
$ git clone https://github.com/gosku/census-scrapper.git
 ```
3. Create virtualenv inside folder
```bash
$ cd census-scrapper 
$ virtualenv --python='python3' env
```
4. Activate virtualenv
```bash
$ source env/bin/activate
 ```
5. Install python dependencies
```bash
$ pip install -r requirements.txt
 ```
## Usage
```bash
$ cd census-scrapper
$ export PATH=$PATH:.
$ source env/bin/activate
$ python app.py
```
