# Day 20: 🛠 A times-table quiz that catches you

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (keep a score)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

It asks you questions in the terminal: type your answer and press Enter.

## What it means

- `int(input(...))` asks a question and turns your answer from text into a number.
- `if ans == 7 * 8:` compares your answer with `7 * 8`. Python does not remember the answer: it works it out by itself.
- **Tab = 4 spaces.** A line pushed in by 4 spaces belongs to the line above it that ends with `:`
  (`if`, `else`, `for`). It only runs when that line says so.
- `else:` runs when the `if` was not true: a wrong answer → `Caught you!`
- In the `for` loop, `i` is 1, 2, 3, and `f"7x{i}? "` puts that number into the question.
- `!=` means "not equal".

## Your turn

At the end, say how many answers were right: `score = 0` before the loop, `score = score + 1` after every
`Correct!`, and `print(score)` at the end. The answer is in `exercise.py`.

---

<div dir="rtl">

# روز 20: 🛠 آزمون جدول ضرب که مچت رو می‌گیره

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (شمردن جواب‌های درست)

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.)

## یعنی چی؟

- ⁦`int(input(...))`⁩ یه سؤال می‌پرسه و جوابت رو از متن، عدد می‌کنه.
- ⁦`if ans == 7 * 8:`⁩ جوابت رو با ⁦`7 * 8`⁩ مقایسه می‌کنه. پایتون جواب رو حفظ نکرده؛ خودش ضرب می‌کنه.
- **Tab یعنی 4 تا فاصله.** خطی که 4 فاصله جلوتره، زیرمجموعه‌ی خط بالاییه که با ⁦`:`⁩ تموم شده (⁦`if`⁩، ⁦`else`⁩، ⁦`for`⁩)؛ فقط وقتی اون خط بگه، اجرا می‌شه.
- ⁦`else:`⁩ وقتی اجرا می‌شه که ⁦`if`⁩ درست نبود: جواب غلط ← ⁦`Caught you!`⁩
- توی حلقه‌ی ⁦`for`⁩، ⁦`i`⁩ می‌شه 1، 2، 3 و ⁦`f"7x{i}? "`⁩ اون عدد رو می‌ذاره توی سؤال.
- ⁦`!=`⁩ یعنی «مساوی نیست».

## نوبت توئه

آخرش بگه چند تا جواب درست بود: قبل از حلقه ⁦`score = 0`⁩، بعد از هر ⁦`Correct!`⁩ ⁦`score = score + 1`⁩، و آخر کار ⁦`print(score)`⁩. جوابش توی ⁦`exercise.py`⁩ ـه.

</div>
