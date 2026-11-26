# Day 27: dictionaries (the wedding gift notebook)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `{"Ali": 500, "Sara": 300}` in curly brackets `{ }` is a **dictionary**: like a notebook where every name has one value next to it.
- The name on the left is the **key** (`"Ali"`), the number on the right is its **value** (`500`).
- `gifts["Sara"]` gives the value of the key `"Sara"`: `300`. No searching, Python goes straight to it.
- `"Ali" in gifts` asks: is this key in the dictionary? `True` means yes, `False` means no. So `"Reza" in gifts` is `False`: Reza gave no gift!
- Asking for a key that is not there, like `gifts["Reza"]`, stops with a `KeyError`. That's why we check with `in` first.

## Exercise

Put the ages of three friends in a dictionary, then print one of the ages. Comment your code!

---

<div dir="rtl">

# روز 27: دیکشنری (دفتر کادوی عروسی)

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (اول خودت امتحان کن!)

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.)

## یعنی چی؟

- ⁦`{"Ali": 500, "Sara": 300}`⁩ با آکولاد ⁦`{ }`⁩ یه **دیکشنری** ـه: مثل یه دفتر که جلوی هر اسم، یه مقدار نوشته.
- اسمِ سمت چپ **کلید** ـه (⁦`"Ali"`⁩)، عددِ سمت راست **مقدار** (⁦`500`⁩).
- ⁦`gifts["Sara"]`⁩ مقدارِ کلید ⁦`"Sara"`⁩ رو می‌ده: ⁦`300`⁩. بدون گشتن؛ پایتون مستقیم می‌ره سراغش.
- ⁦`"Ali" in gifts`⁩ می‌پرسه: این کلید توی دیکشنری هست؟ ⁦`True`⁩ یعنی هست، ⁦`False`⁩ یعنی نیست. پس ⁦`"Reza" in gifts`⁩ می‌شه ⁦`False`⁩: رضا کادو نداد!
- اگه کلیدی رو بخوای که نیست، مثل ⁦`gifts["Reza"]`⁩، با خطای ⁦`KeyError`⁩ وایمیسه. برای همین اول با ⁦`in`⁩ چک می‌کنیم.

## تمرین

سن سه تا دوستت رو بذار توی یه دیکشنری و سن یکی‌شون رو چاپ کن. کدت رو کامنت کن!

</div>
