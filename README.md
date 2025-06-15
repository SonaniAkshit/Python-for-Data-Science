Python has **many built-in and external libraries** that serve different purposes—like working with dates, math, web, files, images, data science, AI, and more.

Below is a categorized list of **popular Python libraries**, along with a **small example** for each.

---

## 🧮 **1. Standard (Built-in) Libraries**

These come pre-installed with Python.

| Library      | Purpose                                | Example                          |
| ------------ | -------------------------------------- | -------------------------------- |
| `calendar`   | Date calendar generation               | `calendar.month(2025, 6)`        |
| `datetime`   | Working with dates & times             | `datetime.now()`                 |
| `math`       | Math functions                         | `math.sqrt(16)`                  |
| `random`     | Random number generation               | `random.randint(1, 10)`          |
| `os`         | Interact with OS (files, dirs)         | `os.listdir()`                   |
| `sys`        | System-specific params/functions       | `sys.exit()`                     |
| `json`       | Working with JSON data                 | `json.dumps({"name": "Akshit"})` |
| `re`         | Regular expressions                    | `re.search("a", "apple")`        |
| `time`       | Time-related functions                 | `time.sleep(2)`                  |
| `statistics` | Stats functions                        | `statistics.mean([1, 2, 3])`     |
| `itertools`  | Iterators (combinations, permutations) | `itertools.permutations([1, 2])` |

---

## 📦 **2. External Libraries** (Need installation using `pip`)

### 📊 Data Science & Machine Learning

| Library        | Purpose                     | Example                      |
| -------------- | --------------------------- | ---------------------------- |
| `numpy`        | Numeric arrays, math ops    | `np.array([1,2,3])`          |
| `pandas`       | DataFrames & data handling  | `pd.read_csv("data.csv")`    |
| `matplotlib`   | Plotting graphs             | `plt.plot([1,2,3])`          |
| `seaborn`      | Advanced data visualization | `sns.histplot(data)`         |
| `scikit-learn` | ML algorithms               | `model.fit(X, y)`            |
| `tensorflow`   | Deep learning               | `tf.constant([1,2])`         |
| `keras`        | Neural networks             | `model = keras.Sequential()` |
| `xgboost`      | Gradient boosting           | `xgboost.train()`            |

### 📊 Example:

```python
import numpy as np
a = np.array([1, 2, 3])
print(a.mean())
```

---

### 🌐 Web Development

| Library          | Purpose             | Example                              |
| ---------------- | ------------------- | ------------------------------------ |
| `flask`          | Micro web framework | `Flask(__name__)`                    |
| `django`         | Full web framework  | `python manage.py runserver`         |
| `requests`       | HTTP requests       | `requests.get("https://api")`        |
| `beautifulsoup4` | Web scraping        | `BeautifulSoup(html, "html.parser")` |
| `selenium`       | Browser automation  | `webdriver.Chrome()`                 |

---

### 🧠 AI / NLP / Chatbot

| Library        | Purpose                            | Example                        |
| -------------- | ---------------------------------- | ------------------------------ |
| `nltk`         | Natural Language Processing        | `nltk.word_tokenize(text)`     |
| `spacy`        | NLP + Named Entity Recognition     | `spacy.load("en_core_web_sm")` |
| `transformers` | Pretrained models from HuggingFace | `pipeline("text-generation")`  |

---

### 📁 File Handling / Utilities

| Library    | Purpose                | Example                         |
| ---------- | ---------------------- | ------------------------------- |
| `openpyxl` | Read/write Excel files | `load_workbook("file.xlsx")`    |
| `csv`      | Work with CSV files    | `csv.reader(open("file.csv"))`  |
| `shutil`   | File operations        | `shutil.copy("a.txt", "b.txt")` |
| `zipfile`  | Zip files              | `zipfile.ZipFile('a.zip')`      |

---

### 🔐 Cybersecurity / Encryption

| Library        | Purpose    | Example                    |
| -------------- | ---------- | -------------------------- |
| `hashlib`      | Hashing    | `hashlib.sha256(b"hello")` |
| `cryptography` | Encryption | `Fernet(key).encrypt()`    |

---

### 📷 Images / Audio / Video

| Library   | Purpose         | Example                      |
| --------- | --------------- | ---------------------------- |
| `Pillow`  | Image handling  | `Image.open("img.jpg")`      |
| `opencv`  | Computer vision | `cv2.imread("img.jpg")`      |
| `pyaudio` | Audio recording | `pyaudio.Stream()`           |
| `moviepy` | Video editing   | `VideoFileClip("video.mp4")` |

---

## 🧰 Other Useful Libraries

| Library             | Purpose                | Example                              |
| ------------------- | ---------------------- | ------------------------------------ |
| `argparse`          | Command-line arguments | `argparse.ArgumentParser()`          |
| `logging`           | Logs and debugging     | `logging.info("test")`               |
| `tkinter`           | GUI building           | `tk.Tk()`                            |
| `threading`         | Multithreading         | `threading.Thread()`                 |
| `multiprocessing`   | Multi-core processing  | `Process(target=func)`               |
| `dotenv`            | Environment variables  | `load_dotenv()`                      |
| `pyttsx3`           | Text to speech         | `pyttsx3.init().say("Hi")`           |
| `speechrecognition` | Convert speech to text | `recognizer.recognize_google(audio)` |

---

## 🧪 BONUS: Install Any External Library

```bash
pip install <library-name>
```

Example:

```bash
pip install numpy
```

---

Would you like a **PDF version** or **interactive notebook** of this list for offline study?
