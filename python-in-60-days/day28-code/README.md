# Day 28: loop over a dictionary + sum (screen time)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `apps = {"Insta": 4, "YouTube": 2}` is a dictionary: each app name (the key) has its hours a day (the value).
- `for name in apps:` goes over the dictionary and gives the **keys** one by one. `name` is a box that holds one key each round: round 1 `name = "Insta"`, round 2 `name = "YouTube"`.
- `apps[name]` uses the name to take its value, like `gifts["Sara"]` on Day 27. So the loop prints `Insta 4` and `YouTube 2`.
- `apps.values()` gives only the values (the hours), and `sum(...)` adds them up: `6`.
- `h * 365 / 24`: 6 hours a day for 365 days, divided by 24 hours in a day = `91.25` days a year. That's 3 months!

## Exercise

Put your own phone hours in a dictionary, then find how many days a year that is. Comment the number!

---

<div dir="rtl">

# روز 28: حلقه روی دیکشنری + ⁦`sum`⁩ (ساعت‌های گوشی)

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

- ⁦`apps = {"Insta": 4, "YouTube": 2}`⁩ یه دیکشنری ـه: اسم هر برنامه (کلید) و ساعتش در روز (مقدار).
- ⁦`for name in apps:`⁩ روی دیکشنری می‌چرخه و **کلیدها** رو یکی‌یکی می‌ده. ⁦`name`⁩ هر دور یه اسم می‌گیره: دور اول ⁦`"Insta"`⁩، دور دوم ⁦`"YouTube"`⁩.
- ⁦`apps[name]`⁩ با اسم، مقدارش رو برمی‌داره؛ مثل ⁦`gifts["Sara"]`⁩ روز 27. برای همین حلقه چاپ می‌کنه ⁦`Insta 4`⁩ و ⁦`YouTube 2`⁩.
- ⁦`apps.values()`⁩ فقط مقدارها (ساعت‌ها) رو می‌ده و ⁦`sum(...)`⁩ جمعشون می‌کنه: ⁦`6`⁩.
- ⁦`h * 365 / 24`⁩: روزی 6 ساعت، ضرب در 365 روز، تقسیم بر 24 ساعت = ⁦`91.25`⁩ روز در سال. یعنی 3 ماه!

## تمرین

ساعت‌های گوشی خودت رو بذار توی یه دیکشنری و ببین سالی چند روز می‌شه. عددش رو کامنت کن!

</div>
