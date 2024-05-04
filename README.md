# django-language-quiz
Created based on Django tutorial to improve my python and django skills.

Also built to quiz myself on Hungarian that I am relearning. 
Initial focus will be on vocabulary and spelling.

# Technologies, Languages, Frameworks
- Django/Python
- Postgres
- Docker

# Initial features to be added
- Have a table of Hungarian words and English translations
- Web page to add/view/update words.
- Web page to quiz on translations or spellings
- Present some number of questions and gives a final score with a list of any incorrect answers
  - For each randomly selected English word from list
    - Give several options of spellings with differing vowels and allow choice of spellings
    - Or require user to fully type the Hungarian word

For example:
- Is the correct spelling of water in Hungarian viz or víz? 
- Is the word for airplane repűlögep, repülőgep, repülögép, or repülőgép?

# Possible future features
- Split list of words into groupings such as well know, and learning
- Randomly choose words from all groups but prioritize those being learned
- Containerize app and database
- Add other types of Hungarian quizes such as useful phrases or verb conjugations
