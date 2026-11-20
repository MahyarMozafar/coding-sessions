# Day 19: Loop over a string + continue (the code from the video)
# The story: the login says "wrong password", but the change-password page says
# "this is your old password". One common reason: a hidden space was copied too.

# letter by letter: the last line looks empty, because the last letter is a space
for ch in "Mohadese ":
    print(ch)

# skip the space with continue; end="" keeps the letters on one line
for ch in "Mohadese ":
    if ch == " ":
        continue
    print(ch, end="")
print()  # go to a new line after the clean password

# why the site said "wrong": for the computer these two passwords are different
login = "Mohadese "
print(login == "Mohadese")
