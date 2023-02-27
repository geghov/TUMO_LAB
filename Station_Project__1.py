import random

user = input('Enter which story (1,2,3) or it will be random : ')


def st1():
    print('_____________Story 1_____________\n\n')
    story = f'''
It was about {input('Number: ')} {input('Measure of time: ') } ago when I arrived at the hospital in a
{input('Mode of Transportation: ')}. The hospital is a/an {input('Adjective: ')} place, there are a lot
 of {input('Adjective2: ')} {input('Noun: ')} here. There are nurses here who have {input('Color: ')} 
{input('Part of the Body: ') }. If someone wants to come into my room I told them that they have to{input('Verb: ')}
 first. I’ve decorated my room with {input('Number2: ')} {input('Noun2: ')}. Today I talked to a doctor and they
  were wearinga {input('Noun3: ')} on their {input('Part of the Body 2: ') }. I heard that all doctors {input('Verb: ')}
{input('Noun4: ')} every day for breakfast.The most {input('Adjective3: ')} thing about being in the hospital is the
{input('Silly Word: ') } {input('Noun: ')} !
    '''
    return story


def st2():
    print('_____________Story 2_____________\n\n')
    story = f'''This weekend I am going camping with {input('( Proper Noun (Person’s Name)): ')}.
I packed my lantern, sleeping bag, and {input('Noun: ')}. I am so {input('(Adjective (Feeling)): ')} 
to {input('Verb: ')} in a tent. I am {input('(Adjective (Feeling) 2): ')} we might see a(n) {input('Animal: ')},
I hear they’re kind of dangerous. While we’re camping, we are going to hike,
fish, and {input('Verb2: ')}. I have heard that the {input('Color: ')} lake is great for 
{input('( Verb (ending in ing) ): ')}. Then we will {input('(Adverb (ending in ly)): ')} hike
through the forest for {input('Number: ')} {input('Measure of Time: ')}. If I see a
{input('Color: ')} {input('Animal: ')} while hiking, I am going to bring it home as a pet!
At night we will tell {input('Number: ')} {input('Silly Word: ')} stories and roast {input('Noun2: ')}
around the campfire!!
    '''
    return story


def st3():
    print('_____________Story 3_____________\n\n')
    story = f'''
    Dear {input('(Proper Noun (Person’s Name) ): ')}, I am writing to you from a
{input('Adjective: ')} castle in an enchanted forest. I found myself here one 
day after going for a ride on a {input('Color: ')} {input('Animal: ')} in {input('Place: ')}. 
There are {input('Adjective2: ')} {input('(Magical Creature (Plural)): ')} and {input('Adjective3: ')}
{input('(Magical Creature (Plural)2): ')} here! In the {input('Room in a House: ')} there
is a pool full of {input('Noun: ')}. I fall asleep each night on a {input('Noun2: ')} of
{input('(Noun(Plural)3): ')} and dream of {input('Adjective4: ')} {input('(Noun(Plural)4): ')}.
It feels as though I have lived here for {input('Number: ')} {input('Measure of time: ')}.
I hope one day you can visit, although the only way to get
here now is {input('(Verb(ending in ing)): ')} on a {input('Adjective5: ')} {input('Noun5: ')}!!
'''
    return story


wiche = [st1, st2, st3]
if user == '1' or user == '2' or user == '3':
    print(wiche[int(user)-1]())
else:
    print(wiche[random.randint(0, 2)]())
