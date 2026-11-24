# Day 23: Sort and pop (the bakery queue, part 3)

Part 1 of the bakery queue is [Day 21](../day21-code/), part 2 is [Day 22](../day22-code/).

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `tickets.sort()` puts the list in order: numbers from small to big, names from A to Z.
- `tickets.pop(0)` takes out the item at place `0` (the first one in the queue).
- `pop` also **gives back** what it took, so `served = tickets.pop(0)` keeps it in `served`.
- `remove` needs the **value** (the name); `pop` needs the **place number** (the index).

## Exercise

Write `pop()` with no number. Who leaves the queue? Run it and see.

---

<div dir="rtl">

# روز 23: مرتب کردن و برداشتن (صف نونوایی، قسمت سوم)

قسمت اول صف نونوایی [روز 21](../day21-code/) و قسمت دوم [روز 22](../day22-code/) ـه.

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

- ⁦`tickets.sort()`⁩ لیست رو مرتب می‌کنه: عددها از کوچیک به بزرگ، اسم‌ها به ترتیب الفبا.
- ⁦`tickets.pop(0)`⁩ چیزی که توی جای ⁦`0`⁩ ـه (نفر اول صف) رو برمی‌داره.
- ⁦`pop`⁩ چیزی که برداشته رو **پس هم می‌ده**؛ برای همین ⁦`served = tickets.pop(0)`⁩ نگهش می‌داره.
- ⁦`remove`⁩ **اسم** (مقدار) رو می‌خواد؛ ⁦`pop`⁩ **شماره‌ی جا** (ایندکس) رو.

## تمرین

⁦`pop()`⁩ رو بدون عدد بنویس. کی از صف می‌ره؟ اجراش کن و ببین.

</div>
