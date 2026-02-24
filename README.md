# 🤖 Telegram Bots

A collection of educational Telegram bots built using pytelegrambotapi.
This repository contains several small Telegram bots created to explore:
- Telegram Bot API;
- Text processing;
- Automation;
- Basic fuzzy matching (rule-based chatbot).

## Bots Included:

1️⃣ Echo Bot:
Repeats any text message sent by the user.

2️⃣ Wiki Bot:
Returns a short preview (first ~1000 characters) of a Wikipedia article.

Features:
- Configurable language (via environment variable);
- Basic text cleaning;
- Error handling for missing or ambiguous pages.

3️⃣ A or B Bot (Facts / Jokes):
Displays custom keyboard buttons (e.g., Joke / Fact).
When pressed, the bot sends a random line from a corresponding text file.
The bot is fully configurable — you can replace jokes/facts with any custom content.

4️⃣ Auto Post Bot:
Automatically posts messages from a text file to a Telegram channel at a fixed interval.

5️⃣ Simple Chat Bot:
Rule-based chatbot using fuzzy string matching.
It compares user input with predefined phrases and returns the closest match.

## 🛠 Data Configuration:

- For A_or_B Bot:

Create /data folder and create files data/jokes.txt and data/facts.txt with any content you like.
Of course you could change facts or jokes or both to something else, but do not forget to update the bot code.

- For Chat Bot:

Create bot_data/chat.txt with format:
```
u: "message" for user
b: "reply" for bot
```
The bot will match user input to the closes question using fuzzy matching

## 🛠 Requirements:

- Python 3.9+;
- pytelegrambotapi;
- wikipedia;
- fuzzywuzzy;
- python-Levenshtein (optional, for better performance);
- python-dotenv.
