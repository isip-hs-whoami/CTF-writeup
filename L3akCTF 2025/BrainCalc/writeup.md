# L3akCTF - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## BrainCalc / Mobile

>Quick and fun math quiz app for practicing.
>
> [app-debug1.zip](https://github.com/isip-hs-whoami/CTF-writeup/blob/main/L3akCTF%202025/BrainCalc/app-debug1.zip)

### Solution
apk檔案可以直接利用apktool去解開，觀察smali會發現在APP中有Python的直譯器，另外從目錄名稱可以推測應該是放在assets/chaquopy目錄內，並在目錄內找到一個app.imy的檔案，觀察檔案架構可以發現zip的magic number(0x504B0304)，解壓縮後就能獲得pyc檔，利用[pylingual.io](https://pylingual.io/)可以得到python code：

```python=
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random
import zlib
import base64

class MathChallenge(toga.App):
    def startup(self):
        self.current_answer = 0
        self.score = 0
        self.questions_answered = 0
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        title_label = toga.Label('Math Challenge', style=Pack(padding=10, text_align='center', font_size=24, font_weight='bold'))
        self.question_label = toga.Label('Loading question...', style=Pack(padding=15, text_align='center', font_size=18))
        self.answer_input = toga.TextInput(placeholder='Enter your answer here', style=Pack(padding=10, width=200))
        button_box = toga.Box(style=Pack(direction=ROW, padding=10))
        new_question_btn = toga.Button('New Question', on_press=self.generate_question, style=Pack(flex=1, padding=5))
        submit_btn = toga.Button('Submit Answer', on_press=self.check_answer, style=Pack(flex=1, padding=5))
        button_box.add(new_question_btn)
        button_box.add(submit_btn)
        self.result_label = toga.Label('', style=Pack(padding=10, text_align='center', font_size=16))
        self.score_label = toga.Label('Score: 0/0 (0%)', style=Pack(padding=5, text_align='center', font_size=14))
        main_box.add(title_label)
        main_box.add(self.question_label)
        main_box.add(self.answer_input)
        main_box.add(button_box)
        main_box.add(self.result_label)
        main_box.add(self.score_label)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        self.generate_question(None)

    def generate_question(self, widget):
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        if operation == '+':
            a, b = (random.randint(1, 100), random.randint(1, 100))
            self.current_answer = a + b
            question = f'What is {a} + {b}?'
        else:  # inserted
            if operation == '-':
                a, b = (random.randint(50, 150), random.randint(1, 49))
                self.current_answer = a - b
                question = f'What is {a} - {b}?'
            else:  # inserted
                if operation == '*':
                    a, b = (random.randint(1, 15), random.randint(1, 15))
                    self.current_answer = a * b
                    question = f'What is {a} × {b}?'
                else:  # inserted
                    b = random.randint(2, 12)
                    self.current_answer = random.randint(2, 20)
                    a = self.current_answer * b
                    question = f'What is {a} ÷ {b}?'
        self.question_label.text = question
        self.answer_input.value = ''
        self.result_label.text = ''

    async def check_answer(self, widget):
        if not self.answer_input.value:
            await self.main_window.info_dialog('Error', 'Please enter an answer!')
            return
        else:  # inserted
            try:
                user_answer = float(self.answer_input.value)
                self.questions_answered += 1
                if abs(user_answer - self.current_answer) < 0.01:
                    self.score += 1
                    self.result_label.text = 'Correct!'
                    if self.questions_answered >= 10 and self.score == self.questions_answered:
                        await self.main_window.info_dialog('Amazing!', 'Perfect score!')
            except ValueError:
                else:  # inserted
                    self.result_label.text = f'Wrong! The answer was {self.current_answer}'
                percentage = round(self.score / self.questions_answered * 100) if self.questions_answered > 0 else 0
                self.score_label.text = f'Score: {self.score}/{self.questions_answered} ({percentage}%)'
                    await self.main_window.info_dialog('Error', 'Please enter a valid number!')

def get_secret_reward():
    compressed_flag = 'eJzzMXb0rvYqLS6JN4kPNynKjQ8tiHfOMMnJqQUAeHcJQA=='
    try:
        decoded = base64.b64decode(compressed_flag)
        flag = zlib.decompress(decoded).decode('utf-8')
        return flag
    except:
        return 'Error: Could not decode secret'

def main():
    return MathChallenge()
```

執行get_secret_reward()函式(其實就是將flag解壓縮)，最後得到flag:`L3AK{Just_4_W4rm_Up_Ch4ll}`