# Day 24: Loop over a list and `in` (the bakery queue, part 4)

Parts 1-3 of the bakery queue are [Day 21](../day21-code/), [Day 22](../day22-code/) and [Day 23](../day23-code/).

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.) It asks for a name at the end: type `Uncle` and press Enter.

## What it means

- `"Reza" in queue` asks: is `"Reza"` in the list? The answer is `True` (yes) or `False` (no).
- `for name in queue:` goes through the list one by one. In each round, `name` holds the name of that round.
- The line under it is pushed in (4 spaces), so it is **inside** the loop and runs every round.
- At the party door: if your name is `in` the guest list, you get `Welcome!`.

## Exercise

Make a shopping list and print it one by one with `for`.

---

<div dir="rtl">

# روز 24: حلقه روی لیست و ⁦`in`⁩ (صف نونوایی، قسمت چهارم)

قسمت‌های 1 تا 3 صف نونوایی [روز 21](../day21-code/)، [روز 22](../day22-code/) و [روز 23](../day23-code/) ـن.

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (اول خودت امتحان کن!)

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.) آخرش اسم می‌پرسه: بنویس ⁦`Uncle`⁩ و اینتر بزن.

## یعنی چی؟

- ⁦`"Reza" in queue`⁩ می‌پرسه: رضا توی لیست هست؟ جوابش ⁦`True`⁩ (آره) یا ⁦`False`⁩ (نه) ـه.
- ⁦`for name in queue:`⁩ یکی‌یکی روی لیست می‌چرخه. هر دور، اسم اون دور می‌ره توی ⁦`name`⁩.
- خط زیرش جلوتره (4 فاصله)؛ پس **توی** حلقه‌ست و هر دور اجرا می‌شه.
- دم در مهمونی: اگه اسمت توی لیست مهمون‌ها بود، ⁦`Welcome!`⁩ می‌گیری.

## تمرین

یه لیست خرید بساز و با ⁦`for`⁩ یکی‌یکی چاپش کن.

</div>
