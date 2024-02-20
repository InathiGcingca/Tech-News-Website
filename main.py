import requests
import validators
from flask import Flask, render_template, url_for, request, redirect



NEWS_API = '981e13fbf86d4c73aecc0a4308f82641'
URL = 'https://newsapi.org/v2/everything'

app = Flask(__name__)

a_list = []


@app.route('/')
def home():
    parameters = {
        'q': 'tech',
        'apiKey': NEWS_API,
    }

    response = requests.get(url=URL, params=parameters)
    response.raise_for_status()
    data = response.json()['articles']



    for i in range(len(data) - 1):
        if data[i]['title'] != None and data[i]['description'] != None and data[i]['url'] != None and data[i]['urlToImage'] != None and validators.url(data[i]['urlToImage']) == True and data[i]['publishedAt'] != None:
            title = data[i]['title']
            content = data[i]['description']
            url = data[i]['url']
            image_url = data[i]['urlToImage']
            date = data[i]['publishedAt'].split('T')[0]
            new_dict = {'title':title, 'content':content, 'url':url, 'image_url':image_url, 'date':date}
            a_list.append(new_dict)




    return render_template('index.html', news_list = a_list)

@app.route('/search', methods=['GET', 'POST'])
def get_search():
    if request.method == 'POST':
        data = request.form
        for i in range(len(a_list)-1):
            if data['Search'] in a_list[i]['title']:
                return  redirect(a_list[i]['url'],code=302)
    return render_template('index.html', news_list=a_list)
















if __name__ == '__main__':
    app.run(debug=True)
