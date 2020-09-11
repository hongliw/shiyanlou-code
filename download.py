import requests
import os.path as osp
import os

def download(url):
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL"{}"'.format(url))
    
    if req.status_code == 403:
        print('You do noe have the authority to access this page.')
        return

    filename = url.split('/')[-1]
    if not osp.exists(osp.join(os.getcwd(),filename)):
        with open(filename, 'w') as f:
            f.write(req.content.decode('utf-8'))
    else:
        with open(filename, 'a') as f:
            f.write(req.content.decode('utf-8'))
        
    print('Download over.')
    


if __name__ == '__main__':
    url = input('Enter a url')
    download(url)
