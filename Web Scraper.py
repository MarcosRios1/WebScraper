from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):

    print(e)
    

def main():

    url = 'https://realpython.com/'
    response = simple_get(url)
        
    
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        
        filename = None
        while filename is None:
            try:
                filename = input('What would you like to name your saved data file? ')
                save = open('{}.txt' .format(filename),'x')

            except:
                print('That filename already exists')
                filename = None
        
        for h2 in html.select('h2'):
            print(h2.text)
            save.write('{} \n' .format(h2.text))
                                
        save.close()


main()
    






















    
    
