#! python3
import webbrowser,sys
if len(sys.argv)>1:
   address=str(' '.join(sys.argv[1:]))
   webbrowser.open('https://www.google.com/maps/place/'+address)

   
