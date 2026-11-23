# Day 22: Add and remove in a list (the bakery queue, part 2)

Part 1 of the bakery queue is [Day 21](../day21-code/).

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `queue.remove("Reza")` deletes `"Reza"` from the list.
- `queue.append("Ali")` adds `"Ali"` to the **end** of the list (the end of the queue).
- The dot `.` means: tell **this** list to do something.
- `queue.remove("reza")` gives an error: for Python a big `R` and a small `r` are different, so `"reza"` is not in the list.
  **Don't panic at an error: read its last line.** `ValueError: list.remove(x): x not in list` means "it is not in the list".

## Exercise

Take your 5-movie list from Day 21. Add one movie and remove one, then print the list.

---

<div dir="rtl">

# روز 22: اضافه و حذف توی لیست (صف نونوایی، قسمت دوم)

قسمت اول صف نونوایی، [روز 21](../day21-code/) ـه.

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

- ⁦`queue.remove("Reza")`⁩ رضا رو از لیست حذف می‌کنه.
- ⁦`queue.append("Ali")`⁩ علی رو به **ته** لیست اضافه می‌کنه (ته صف).
- نقطه ⁦`.`⁩ یعنی: به **همین** لیست بگو یه کاری بکنه.
- ⁦`queue.remove("reza")`⁩ ارور می‌ده: برای پایتون حرف بزرگ ⁦`R`⁩ با حرف کوچیک ⁦`r`⁩ فرق داره؛ پس ⁦`"reza"`⁩ توی لیست نیست.
  **از ارور نترس؛ خط آخرش رو بخون.** ⁦`ValueError: list.remove(x): x not in list`⁩ یعنی «این توی لیست نیست».

## تمرین

لیست پنج‌تا فیلمِ روز 21 رو بردار. یه فیلم اضافه کن، یکی رو حذف کن و لیست رو چاپ کن.

</div>
