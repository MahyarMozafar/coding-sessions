# Day 21: Lists (a queue: the first one is number 0)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `[ ]` makes a list; commas `,` keep the items apart.
- The number in `queue[0]` is **how many steps from the front**. The first one is 0 steps away, so it is `0`.
- `len(queue)` counts the items: `3`.
- `queue[3]` gives an error: a list of 3 has only `0`, `1`, `2`.
  **Don't panic at an error: read its last line.** `IndexError: list index out of range` means "this number is not in the list".
- `queue[-1]` is the last item.

## Exercise

Put your 5 favourite movies in a list and print the first and the last one.

---

<div dir="rtl">

# روز 21: لیست‌ها (یه صف: نفر اول شماره‌ی صفره)

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

- ⁦`[ ]`⁩ یه لیست می‌سازه؛ ویرگول ⁦`,`⁩ چیزها رو از هم جدا می‌کنه.
- عدد توی ⁦`queue[0]`⁩ یعنی **چند قدم از اول صف**. نفر اول صفر قدم فاصله داره؛ پس ⁦`0`⁩ ـه.
- ⁦`len(queue)`⁩ تعداد رو می‌شمره: ⁦`3`⁩.
- ⁦`queue[3]`⁩ ارور می‌ده: لیستِ سه‌تایی فقط ⁦`0`⁩، ⁦`1`⁩، ⁦`2`⁩ داره.
  **از ارور نترس؛ خط آخرش رو بخون.** ⁦`IndexError: list index out of range`⁩ یعنی «این شماره توی لیست نیست».
- ⁦`queue[-1]`⁩ یعنی آخری.

## تمرین

پنج تا فیلم محبوبت رو توی یه لیست بذار و اولی و آخری رو چاپ کن.

</div>
