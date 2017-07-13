input_name=input("What's your name? ")
start = '''
Do your best to keep your bad day points to a minimum.
You are going to work. You're a young woman working to prove yourself to your coworkers and your boss.
You are about to get onto a crowded train with only one seat open. You're tired from working late the night before and really want the seat.
The open seat is next to a middle-aged man who makes you a little uncomfortable. Are you going to sit down?
'''
sit = '''
You have taken a seat. The man sitting next to you keeps looking in your direction. He begins to ask you very personal questions.
You start to feel more uncomfortable. You look for other seats around, but the train is still full.
You are still a couple of stops away from where you get off. Do you want to exit the train and walk the rest of the way, or bear through the man's
rude questioning and try to ignore him?
'''
stand ='''
You have chosen to stand. It is going to be a long ride and you're only going to get more tired. Within an hour you are at your stop.
'''
leave ='''
You chose to leave the train. It's a long walk, and it looks like you're going to be late. There's no time to wait for other transportation,
so you have to try your best to make it on time. Hopefully your boss won't get too angry.
'''
stay='''
You chose to stay on the train. The man sitting next to you continues to bother you throughout the entire ride. By the time you reach your stop,
your patience is thin.
'''
common_office= '''
You have arrived at the office. Your day hasn't started off great, but you have faith that you can turn it around at your conference meeting
today. You have some great ideas that you're ready to share. You enter the meeting eager to begin. However, when you start to share your best
idea you're interrupted by a couple of coworkers. Do you stand up to them and press forward or just give up?
'''

print(start)
done=False
a=False
bad_day=0
while not done:
    print("Type 'sit' to sit down or 'stand' to stay standing. ")
    user_input = input()
    if user_input == "sit":
        print(sit)
        done=True
        while not a:
            print("Type 'leave' to get off the train and walk the rest of the way or type 'stay' to bear through it. ")
            user_input = input()
            if user_input == "leave":
                print(leave)
                bad_day+=3
                print("Bad Day:" + str(bad_day))
                print(common_office)
                a=True
            elif user_input == "stay":
                print(stay)
                bad_day+=2
                print("Bad Day:" + str(bad_day))
                print(common_office)
                a=True
            else:
                print("Try again in the correct format.")

    elif user_input == "stand":
        print(stand)
        bad_day+=1
        print("Bad Day:" + str(bad_day))
        print(common_office)
        done=True
    else:
        print("Try again in the correct format.")

stand_up='''
You stood up for yourself. Good for you! Your coworkers seem to have a mixed reaction.
Some of them seem to respect your drive, while others look to be muttering negative things about you. You hear the word 'bossy' being thrown
around. Despite the negative reactions, your boss admires your drive and tells you to meet him in his office. When you get there, he congratulates
you on your presentation and offers you a promotion. He then attempts to take advantage of you and you are forced to make another important
decision. Do you allow him to take advantage of you to protect your job or do you turn him down and risk being fired?
'''
whatever='''
You chose to be passive and your point is never put across. This could mean your project fails in the future and your coworkers won't hesitate
to walk all over you. Your boss calls you into his office, angry that you brought no ideas to the table. You attempt to explain yourself,
but your attempts are in vain. He fires you right then and there.
'''

no_way='''
You curse out your boss and he fires you. You are upset about your job, but happy about your decision.
'''

ok='''
You let it happen in order to keep your job, but you regret it immensely.
Within a few days, you realize you can't stand to work at the office anymore, even though you need a job, and you decide to quit.
'''
common_Reshma='''
You storm out of the office, upset by the day's events, and you happen
to see Reshma! You break down and tell her about your day and everything that happened.
Once you've calmed down, she gives you a hug and offers you a job at Girls Who Code!!
'''

done=False
a=False
while not done:
    print("Type 'stand up' to stand your ground or 'whatever' to give up. ")
    user_input=input()
    if user_input=="stand up":
        print(stand_up)
        bad_day-=2
        print("Bad Day:" + str(bad_day))
        done=True
        while not a:
            print("Type 'no way' to get out of that office or '...' to let it happen. ")
            user_input=input()
            if user_input=="no way":
                print(no_way)
                bad_day+=7
                print("Bad Day:" + str(bad_day))
                print(common_Reshma)
                bad_day=0
                print("Bad Day:" + str(bad_day))
                a=True
            elif user_input=="...":
                print(ok)
                bad_day+=7
                print("Bad Day:" + str(bad_day))
                print(common_Reshma)
                bad_day=0
                print("Bad Day:" + str(bad_day))
                a=True
            else:
                print("Try again in correct format.")
    elif user_input=="whatever":
        print(whatever)
        bad_day+=7
        print("Bad Day:" + str(bad_day))
        print(common_Reshma)
        bad_day=0
        print("Bad Day:" + str(bad_day))
        done=True
    else:
        print("Try again in correct format")
