pip install -r requirements.txt
echo WELCOME TO DRAGONHOST
echo The Original Project by SergeiTregub on GitHub
echo Local hosting websites.
sleep 5
echo Beta version detected
python welcome.py
python read.py
echo NOW ATTEMPTING TO HOST A LOCAL WEBSITE
python3 -m http.server 8080
echo Hosting closed now.
echo Thank you for using DragonHost!
sleep 2
