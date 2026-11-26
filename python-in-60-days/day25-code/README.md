# Day 25: `zip` and `enumerate` (the dinner bill)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `zip(names, pay)` puts two lists side by side and pairs them: the first name with the first amount, the second with the second, and so on.
- `for n, p in zip(names, pay):` takes one pair each round: the name goes into `n`, the money into `p`.
- `enumerate(food)` gives each item a number. `for i, f in enumerate(food):` puts the number in `i` and the food in `f`.
- Python counts from 0 (like list indexes, [Day 21](../day21-code/)), so `i + 1` makes the list start at 1.
- Good to know: if one list is shorter, `zip` stops at the end of the shorter list.

## Exercise

Number your shopping list with `enumerate`, starting from 1.

---

<div dir="rtl">

# روز 25: ⁦`zip`⁩ و ⁦`enumerate`⁩ (دنگ شام)

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

- ⁦`zip(names, pay)`⁩ دو تا لیست رو کنار هم می‌ذاره و جفت می‌کنه: اسم اول با پول اول، دومی با دومی و همین‌طور تا آخر.
- ⁦`for n, p in zip(names, pay):`⁩ هر دور یه جفت برمی‌داره: اسم می‌ره توی ⁦`n`⁩، پولش توی ⁦`p`⁩.
- ⁦`enumerate(food)`⁩ به هر چیز یه شماره می‌ده. ⁦`for i, f in enumerate(food):`⁩ شماره رو می‌ذاره توی ⁦`i`⁩ و غذا رو توی ⁦`f`⁩.
- پایتون از صفر می‌شمره (مثل شماره‌ی خونه‌های لیست، [روز 21](../day21-code/))؛ برای همین ⁦`i + 1`⁩ می‌نویسیم که از 1 شروع شه.
- خوبه بدونی: اگه یکی از لیست‌ها کوتاه‌تر باشه، ⁦`zip`⁩ آخرِ لیست کوتاه‌تر وایمیسه.

## تمرین

لیست خریدت رو با ⁦`enumerate`⁩ شماره‌دار کن؛ از 1 شروع کن.

</div>
