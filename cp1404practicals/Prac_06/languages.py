from programming_languages import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
java = ProgrammingLanguage("Java", "Static", True, 1995)

print(ruby)
print(python)
print(visual_basic)
print(c_plus_plus)
print(java)
print()

languages = [ruby, python, visual_basic, c_plus_plus, java]

print("The dynamically typed languages are:")

for language in languages:
    if language.is_dynamic():
        print(language.name)
