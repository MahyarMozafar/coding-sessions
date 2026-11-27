# Day 29: a list of dictionaries (Divar ads)

- `main.py`: the code from the video
- `exercise.py`: the answer to today's exercise (try it yourself first!)

## Run it

```bash
python main.py
```

(On Mac use `python3` instead of `python`.)

## What it means

- `ad1 = {"name": "A57", "price": 160}` is a dictionary: one ad, like one card with a name and a price (in million toman).
- `ads = [ad1, ad2]` is a **list of dictionaries**: the whole Divar page, a pile of cards. `len(ads)` is `2`.
- `for ad in ads:` brings the cards one by one: round 1 `ad` is the A57 card, round 2 the Redmi card.
- `ad["price"]` takes the price from that card, and `if ad["price"] < 150:` asks: is it under your budget?
- Round 1: 160 < 150? No. Round 2: 140 < 150? Yes, so `print(ad["name"])` prints `Redmi`.

## Exercise

Add one more ad to the list, then run the same search. What did it print? Comment it!

---

<div dir="rtl">

# روز 29: لیستی از دیکشنری‌ها (آگهی‌های دیوار)

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

- ⁦`ad1 = {"name": "A57", "price": 160}`⁩ یه دیکشنری ـه: یه آگهی، مثل یه کارت با اسم و قیمت (میلیون تومان).
- ⁦`ads = [ad1, ad2]`⁩ یه **لیست از دیکشنری‌ها**ست: کل صفحه‌ی دیوار، یه دسته کارت. ⁦`len(ads)`⁩ می‌شه ⁦`2`⁩.
- ⁦`for ad in ads:`⁩ کارت‌ها رو یکی‌یکی میاره: دور اول ⁦`ad`⁩ کارت A57 ـه، دور دوم کارت ردمی.
- ⁦`ad["price"]`⁩ قیمت همون کارت رو برمی‌داره و ⁦`if ad["price"] < 150:`⁩ می‌پرسه: زیر بودجه‌ته؟
- دور اول: 160 کمتر از 150؟ نه. دور دوم: 140 کمتر از 150؟ آره؛ پس ⁦`print(ad["name"])`⁩ چاپ می‌کنه ⁦`Redmi`⁩.

## تمرین

یه آگهی دیگه به لیست اضافه کن و همون جستجو رو اجرا کن. چی چاپ شد؟ کامنت کن!

</div>
