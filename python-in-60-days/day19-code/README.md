# Day 19: Loop over a string + continue (the hidden space in a password)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## The story

The login says "wrong password". You go to change it, and the site says "this is your old password".
One common reason: when you copied the password, a hidden space was copied too.

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

You should see:

```text
M
o
h
a
d
e
s
e
 
Mohadese
False
```

## What it means

- `for ch in "Mohadese "` gives one letter in every round. `ch` is a name we chose: you can write `letter` or any name you like. The text can be anything too.
- `print(ch)` is written further in, so it belongs to the loop and runs every round. The last line looks empty: that letter is a space.
- `if ch == " ":` asks: is this letter a space?
- `continue` skips the rest of this round and goes to the next letter.
- `print(ch, end="")` writes the letters next to each other, on one line (no new line after each letter).
- `login == "Mohadese"` is `False`: for the computer, a password with a space and one without it are two different passwords.

Other common reasons for "wrong password": Caps Lock is on, or the keyboard is in Persian.

## Exercise

Remove the hidden spaces from `" Moha dese "` with Python.

---

<div dir="rtl">

# روز 19: حلقه روی متن و ⁦`continue`⁩ (فاصله‌ی قایم توی رمز)

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (اول خودت امتحانش کن!)

## داستان

صفحه‌ی ورود می‌گه «رمز اشتباه است». می‌ری رمز رو عوض کنی، سایت می‌گه «این رمز قبلیته».
یکی از دلیل‌های رایجش: وقتی رمز رو کپی کردی، یه فاصله‌ی قایم هم کپی شد.

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.)

## یعنی چی؟

- ⁦`for ch in "Mohadese "`⁩ هر دور یه حرف می‌ده. ⁦`ch`⁩ اسمیه که خودمون انتخاب کردیم: می‌تونی بنویسی ⁦`letter`⁩ یا هر اسمی که دوست داری. متن رو هم هر چی بخوای می‌تونی بنویسی.
- ⁦`print(ch)`⁩ جلوتر نوشته شده؛ یعنی مال حلقه‌ست و هر دور اجرا می‌شه. خط آخر خالی به نظر میاد: اون حرف، یه فاصله‌ست.
- ⁦`if ch == " ":`⁩ می‌پرسه: این حرف فاصله‌ست؟
- ⁦`continue`⁩ بقیه‌ی این دور رو رد می‌کنه و می‌ره سراغ حرف بعدی.
- ⁦`print(ch, end="")`⁩ حرف‌ها رو کنار هم، توی یه خط می‌نویسه (بعد از هر حرف خط جدید نمی‌ره).
- ⁦`login == "Mohadese"`⁩ می‌شه ⁦`False`⁩: برای کامپیوتر، رمز با فاصله و رمز بی‌فاصله، دو تا رمز جدان.

دلیل‌های رایج دیگه برای «رمز اشتباه است»: ⁦Caps Lock⁩ روشنه، یا کیبورد فارسیه.

## تمرین

فاصله‌های قایم ⁦`" Moha dese "`⁩ رو با پایتون پاک کن.

</div>
