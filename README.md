Telegram Bots

A collection of educational Telegram bots built using pytelegrambotapi.
This repository contains several small Telegram bots created to explore:
(i) Telegram Bot API
(ii) Text processing
(iii) Automation
(iv) Basic fuzzy matching (rule-based chatbot)

Bots Included
1️⃣ Echo Bot:
Repeats any text message sent by the user.

2️⃣ Wiki Bot:
Returns a short preview (first ~1000 characters) of a Wikipedia article.

Features:
(i) Configurable language (via environment variable)
(ii) Basic text cleaning
(iii) Error handling for missing or ambiguous pages

3️⃣ A or B Bot (Facts / Jokes):
Displays custom keyboard buttons (e.g., Joke / Fact).
When pressed, the bot sends a random line from a corresponding text file.
The bot is fully configurable — you can replace jokes/facts with any custom content.

4️⃣ Auto Post Bot:
Automatically posts messages from a text file to a Telegram channel at a fixed interval.

5️⃣ Simple Chat Bot:
Rule-based chatbot using fuzzy string matching.
It compares user input with predefined phrases and returns the closest match.
