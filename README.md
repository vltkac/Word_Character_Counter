# Word and Character Counter

## Description
This program analyzes a text file and collects statistics:  
- Letter frequency (excluding spaces and punctuation)  
- Total number of words  
- Word frequency  
- Top-5 most frequent words  

Results are saved to `summary.json` and can also be displayed in the console.  

---

## Installation and Usage

1. Place the script `main.py` and a text file for analysis (e.g., `input.txt`) in the same folder.
2. Run the script:

```bash
python main.py
```

3. Enter the file name (or full path) when prompted.
4. Choose one of the menu options:

- `1` — Count letters frequency  
- `2` — Count total words  
- `3` — Count word frequency  
- `4` — Generate full summary and save to JSON  
- `5` — Exit  

---

## Input File Format
The text file (`.txt`) can contain any text. Example:

```
Hello world! This is a test.
This test contains words, letters, and punctuation.
```

---

## Output Format
The program creates a `summary.json` file with the following structure:

```json
{
    "Letters count": { "a": 5, "b": 2, ... },
    "Total words quantity": 20,
    "Words count": { "hello": 1, "world": 1, ... },
    "Top-5 words": [["test", 2], ["this", 2], ["hello", 1], ["world", 1], ["contains", 1]]
}
```

---

## Features
- Case-insensitive word counting  
- Removes punctuation around words  
- Interactive menu allows choosing specific functions without restarting the script  

---

## Note
You need a text file (e.g., `input.txt`) in the same folder, or provide the full path to a text file when prompted.
