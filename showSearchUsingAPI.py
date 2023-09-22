import requests,json,pprint,webbrowser
word = input("Enter Show Name:")
url="https://api.tvmaze.com/singlesearch/shows"
parameter={"q":word}
response=requests.get(url,parameter)
show_data=json.loads(response.text)
name=show_data['name']
lang=show_data['language']
rating=show_data['rating']['average']
prem=show_data['premiered']
summary=show_data['summary']
#pprint.pprint(show_data)
print(f"{name} was premiered on :{prem}, \nRating:{rating},\nLanguage:{lang}","\nGenre:",*show_data['genres'])
print("Summary:",summary)
print("\n\n Show is opened in new tab , ENJOY! ;)\n")
a=word.split()
s=""
for i in a:
    s+=i
    s+="+"
s=s[:len(s)-1]
s=s.casefold()
print("https://fmovies.to/filter?keyword="+s)
webbrowser.open_new_tab("https://fmovies.to/filter?keyword="+s)

