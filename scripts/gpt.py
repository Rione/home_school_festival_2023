#!/usr/bin/env python3
import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

def throwPrompt(prompt: str):
    response =  g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.GptGo,
        messages=[{"role": "user", "content": "Please extract a color name from the following sentence and return it in English. Only return the name and never add any other information: "+prompt}],
        stream = True
    )

    for message in response:
        print(message, flush=True, end='')

while True:
    prompt = input('\n<< ')
    if(prompt=='exit'): exit() 
    throwPrompt(prompt)

