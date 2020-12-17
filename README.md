# ShortURl
This is my URL shortener.\n
It uses a django backend and a react frontend.
The principle is very simple, you type the URI you want to shorten
and press the button. Now a random code gets generated, inserted into
a sqlite database and referenced to the "old" URI. Now when you go to
r/{code}, where code is the randomly generated code, which is in the link 
shown after shortening, you get redirected to the URl your "old" URI.
