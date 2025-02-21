import random
def option(opt_user, opt_bot) :
    if (opt_user == 1 and opt_bot == 2) :
        return "You"
    elif (opt_user == 2 and opt_bot == 3) :
        return "You"
    elif (opt_user == 3 and opt_bot == 1) :
        return "You"
    elif (opt_bot == opt_user) :
        print("Draw!")
    else :
        return "Bot"
opt_bot = random.randint(1,3)
opt_user = int(input("1. Snake\n2. Water\n3. Gun\nEnter your choice: "))
print("Bot chose: ",opt_bot)
print("Round won by: ",option(opt_user,opt_bot))
