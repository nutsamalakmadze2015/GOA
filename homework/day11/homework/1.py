# input დავალებები:
# 1)დაწერეთ პროგრამა, რომელიც ითხოვს მომხმარებლის სახელს და ამის შემდეგ ბეჭდავს: 
# "გამარჯობა, სახელი!"(გაიხსენეთ day1 დავალება)
name = input("please enter your name: ")
print("hello"+" " + name + "!")
# 2)მომხმარებელს შემოატანინეთ მასზე ინფორმაცია და ეს ყველაფერი ერთ print-ში დაბეჭდეთ
info = input("please enter your info: ")
print(info)
# 3)შემოატანინეთ მომხარებელს პაროლი და დაბეჭდეთ ეგ პაროლი თუ შემოტანილი პაროლი უდრის თქვენთვის სასურველ 
# პაროლს მაშინ უნდა გამოიტანოს True თუ არა False
pasword = input("please enter your pasword: ")
if pasword == "nuca1790":
    print("True")
else:
    print("False")

# ლოგიკური ოპერაციებზე დავალებები:
# 4)and-ის გამოყენებით გააკეთეთ  boolean მაგალითები მაგალითად True and False და ასე შემდეგ კომენტარში ახსენით 
# თუ რატო გამოდის ეგეთი  შედეგი როგორიცაა False
print(False and False)#False იმიტომ რომ არცერთ პირობას არ ვაკმაყოფილებთ
print(True and False)#False იმიტომ რომ ერთ პირობას არ ვაკმაყოფილებთ
print(True and True)#True იმიტომ რომ ორივე პირობას არ ვაკმაყოფილებთ
print(False and True)#False იმიტომ რომ ერთ პირობას არ ვაკმაყოფილებთ



