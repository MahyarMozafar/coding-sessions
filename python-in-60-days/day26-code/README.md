# Day 26: sets and tuples (how rond is your number?)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.) The last line stops with a `TypeError` on purpose: that is the lesson.

## What it means

- `set(a)` keeps only one of each item. For the text `"09121111111"` that is the digits 0, 9, 1 and 2.
- `len(...)` counts them. Fewer different digits = a more "rond" number.
- A set has no fixed order, so we count it with `len` instead of printing it.
- `(1375, 6, 12)` in round brackets is a **tuple**: like a list, but locked. You can read it (`birthday[0]` is 1375), but you can't change it.
- `birthday[0] = 1385` gives `TypeError`: a tuple can't be changed. Don't panic: the error tells you exactly that.

## Exercise

Count the different digits of your own phone number. Comment only the count, never your number!

---

<div dir="rtl">

# روز 26: ⁦`set`⁩ و ⁦`tuple`⁩ (شماره‌ت چقدر رنده؟)

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (اول خودت امتحان کن!)

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.) خط آخر عمداً با ⁦`TypeError`⁩ وایمیسه: درس امروز همینه.

## یعنی چی؟

- ⁦`set(a)`⁩ از هر چیز فقط یکی نگه می‌داره. برای ⁦`"09121111111"`⁩ می‌شه رقم‌های 0، 9، 1 و 2.
- ⁦`len(...)`⁩ می‌شمره‌شون. هر چی رقم‌های مختلف کمتر، شماره رندتر.
- ترتیبِ ⁦`set`⁩ ثابت نیست؛ برای همین با ⁦`len`⁩ می‌شمریمش، نه این‌که چاپش کنیم.
- ⁦`(1375, 6, 12)`⁩ با پرانتز یه **tuple** ـه: مثل لیست، ولی قفل. می‌شه خوندش (⁦`birthday[0]`⁩ می‌شه 1375) ولی نمی‌شه عوضش کرد.
- ⁦`birthday[0] = 1385`⁩ خطای ⁦`TypeError`⁩ می‌ده: ⁦`tuple`⁩ عوض نمی‌شه. نترس؛ خطا دقیقاً همینو می‌گه.

## تمرین

رقم‌های مختلف شماره‌ی خودت رو بشمار. فقط عددش رو کامنت کن، نه خود شماره رو!

</div>
