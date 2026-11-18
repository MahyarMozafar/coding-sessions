# Day 18: Nested loops (a loop inside a loop)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

The small cinema prints:

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

Then the real cinema prints 200 lines, from `1 1` to `10 20`.

## What it means

- The first loop counts the rows: 1 and 2.
- The second loop is written a little further to the right, so it is **inside** the first loop. It counts the seats: 1, 2, 3.
- For every row, the inner loop runs again from the start. So 2 rows x 3 seats = 6 lines.
- For the real cinema only two numbers change: 10 rows x 20 seats = 200 seats.

## Exercise

Make a cinema with 3 rows and 4 seats in each row. How many seats does it have?

---

<div dir="rtl">

# روز 18: حلقه توی حلقه

- ⁦`main.py`⁩: کد داخل ویدیو
- ⁦`exercise.py`⁩: جواب تمرین امروز (اول خودت امتحانش کن!)

## اجرا

</div>

```bash
python main.py
```

<div dir="rtl">

(در مک به‌جای ⁦`python`⁩ بنویس ⁦`python3`⁩.)

سینمای کوچیک این رو چاپ می‌کنه:

</div>

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

<div dir="rtl">

بعد سینمای واقعی دویست خط چاپ می‌کنه، از ⁦`1 1`⁩ تا ⁦`10 20`⁩.

## یعنی چی؟

- حلقه‌ی اول ردیف‌ها رو می‌شمره: یک و دو.
- حلقه‌ی دوم یه کم جلوتر نوشته شده، پس **توی** حلقه‌ی اوله. صندلی‌ها رو می‌شمره: یک، دو، سه.
- برای هر ردیف، حلقه‌ی داخلی از اول کامل می‌چرخه. پس دو ردیف ضرب‌در سه صندلی، می‌شه شش خط.
- برای سینمای واقعی فقط دو تا عدد عوض می‌شه: ده ردیف ضرب‌در بیست صندلی، می‌شه دویست صندلی.

## تمرین

یه سینما با سه ردیف و چهار صندلی بساز. چند تا صندلی داره؟

</div>
