# Cheat sheet: Day 11–20 (decisions and loops)

<div dir="rtl">

# جزوه‌ی روز 11 تا 20: شرط‌ها و حلقه‌ها

همه‌ی چیزهایی که توی این ده روز یاد گرفتیم، توی یه صفحه. ذخیره‌ش کن!

## مقایسه (روز 11)

</div>

```python
print(7 > 3)     # True   bigger
print(2 < 9)     # True   smaller
print(5 == 5)    # True   equal?
print(5 != 5)    # False  not equal?
print(5 >= 5)    # True   bigger or equal
```

<div dir="rtl">

- یه مساوی ⁦`=`⁩ یعنی «بذار توی متغیر». دو تا مساوی ⁦`==`⁩ یعنی «مقایسه کن».
- جواب همیشه ⁦`True`⁩ یا ⁦`False`⁩ ـه.

## شرط: ⁦`if / elif / else`⁩ (روز 12 و 13)

</div>

```python
score = 17
if score >= 18:
    print("Great")
elif score >= 12:
    print("Good")
else:
    print("Try again")
```

<div dir="rtl">

- آخر خط ⁦`if`⁩ و ⁦`elif`⁩ و ⁦`else`⁩ دو نقطه ⁦`:`⁩ می‌ذاریم.
- خط‌های داخلش یه Tab (یعنی 4 تا فاصله) می‌رن جلو؛ یعنی زیرمجموعه‌ی همون خط‌ان و فقط وقتی اون شرط درسته، اجرا می‌شن.
- پایتون از بالا چک می‌کنه؛ اولین شرط درست اجرا می‌شه.

## چند تا شرط با هم: ⁦`and`⁩ ⁦`or`⁩ ⁦`not`⁩ (روز 14)

</div>

```python
age = 25
print(age >= 18 and age < 30)   # True   both must be true
print(age < 18 or age > 60)     # False  one is enough
print(not age >= 18)            # False  the opposite
```

<div dir="rtl">

## باقی‌مونده با ⁦`%`⁩ (روز 15)

</div>

```python
print(7 % 2)   # 1  -> odd
print(8 % 2)   # 0  -> even
```

<div dir="rtl">

## حلقه‌ی ⁦`for`⁩ و ⁦`range()`⁩ (روز 16)

</div>

```python
for i in range(5):       # 0 1 2 3 4
    print(i)

for i in range(1, 6):    # 1 2 3 4 5
    print(i)
```

<div dir="rtl">

- اگه فقط یه عدد بدی، ⁦`range`⁩ از صفر می‌شمره.
- عدد آخر هیچ‌وقت حساب نمی‌شه: ⁦`range(1, 6)`⁩ تا 5 می‌ره.
- ⁦`i`⁩ هر دور، عدد بعدی رو می‌گیره.

## حلقه‌ی ⁦`while`⁩ و ⁦`break`⁩ (روز 17)

</div>

```python
n = 3
while n > 0:          # repeat while this is true
    print(n)          # 3 / 2 / 1
    n = n - 1         # take one from n
print("Go!")

# the phone lock
while True:           # repeat forever...
    pin = input("PIN? ")
    if pin == "1234":
        break         # ...until break: leave the loop
print("Welcome!")
```

<div dir="rtl">

- ⁦`n = n - 1`⁩ یعنی: یکی از ⁦`n`⁩ کم کن و دوباره بذارش توی ⁦`n`⁩. بدون این خط، حلقه هیچ‌وقت تموم نمی‌شه.
- ⁦`while True`⁩ همیشه تکرار می‌شه؛ فقط ⁦`break`⁩ می‌تونه ازش بیاد بیرون.

## حلقه توی حلقه (روز 18)

</div>

```python
for row in range(1, 3):          # 2 rows
    for seat in range(1, 4):     # 3 seats in every row
        print(row, seat)         # 1 1 / 1 2 / 1 3 / 2 1 / 2 2 / 2 3
```

<div dir="rtl">

- حلقه‌ی بیرونی ردیف‌ها رو می‌شمره، حلقه‌ی داخلی صندلی‌های هر ردیف رو.
- 2 ردیف × 3 صندلی = 6 خط. سینمای واقعی: 10 × 20 = 200 صندلی!

## حلقه روی متن و ⁦`continue`⁩ (روز 19)

</div>

```python
for ch in "Mohadese ":       # one letter in every round
    if ch == " ":
        continue             # skip the space, go to the next round
    print(ch, end="")        # letters side by side
print()                      # Mohadese

login = "Mohadese "
print(login == "Mohadese")   # False: the hidden space makes them different
```

<div dir="rtl">

- ⁦`continue`⁩ یعنی: این دور رو رد کن، برو دور بعد. (⁦`break`⁩ کل حلقه رو تموم می‌کنه.)
- ⁦`end=""`⁩ یعنی: بعد از هر حرف نرو خط بعد.
- یه فاصله‌ی مخفی، رمز رو عوض می‌کنه؛ برای همین گاهی رمز درست «اشتباهه»!

<div dir="rtl">

## پروژه: آزمونی که مچت رو می‌گیره (روز 20)

</div>

```python
for i in range(1, 4):
    ans = int(input(f"7x{i}? "))   # 7x1? 7x2? 7x3?
    if ans == 7 * i:               # Python multiplies by itself
        print("Correct!")
    else:
        print("Caught you!")
```

<div dir="rtl">

- ⁦`!=`⁩ یعنی «مساوی نیست»؛ برعکس ⁦`==`⁩.
- ⁦`f"7x{i}? "`⁩ عدد ⁦`i`⁩ رو می‌ذاره توی سؤال.

## پروژه‌ها

- روز 15: زوج یا فرد؟ ← پوشه‌ی ⁦`day15-code`⁩
- روز 20: آزمون جدول ضرب ← پوشه‌ی ⁦`day20-code`⁩

فاز دو تموم شد 🎉 فاز بعدی: لیست‌ها و دیکشنری‌ها.

</div>
