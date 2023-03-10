from bs4 import BeautifulSoup
import urllib.request

import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text   = True,
        shell  = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)

def main():
    pattern = 'Original'

    url         = f'https://leagueoflegends.fandom.com/wiki/League_of_Legends:_Wild_Rift'
    html_page   = urllib.request.urlopen(url)
    soup        = BeautifulSoup(html_page, 'html.parser')

    for a in soup.find_all('a', href=True):
        img_tag = a.findChildren('img')

        try:
            link_img = img_tag[0]["data-src"]

            if pattern in link_img:
                link_img  = link_img.split("20?")
                name_hero = img_tag[0]['alt'].replace(" ","_").replace("'","")
                runcmd(f'wget -O data/data_train/{name_hero}_20.jpg {link_img[0]}/40', verbose = True)
        except:
            pass

if __name__ == "__main__":
    main()