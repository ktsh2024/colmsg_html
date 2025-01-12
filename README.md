This program creates HTML files for viewing colmsg files.

For example, if you save the colmsg files in below folders:
  C:\Prog\colmsg\data\日木坂26\白石七瀬
  C:\Prog\colmsg\data\日木坂26\加藤京子
  ...
  
and you want to create HTML files in below folder
  C:\Prog\colmsg\html\日木坂26

Then you will run the program in the command line:  
colmsg_html "C:\Prog\colmsg\data\日木坂26" "C:\Prog\colmsg\html\日木坂26"

Then you will find the HTML files by month in the folders:
C:\Prog\colmsg\html\日木坂26\日木坂26-白石七瀬\日木坂26-白石七瀬YYYYMM.html
C:\Prog\colmsg\html\日木坂26\日木坂26-加藤京子\日木坂26-加藤京子YYYYMM.html

You may also put your nick name at the end of the command.  Otherwise "としくん" will be used as default.

If you want to run the program in a script, remember to add "chcp 65001" to recognize unicode characters.  (see run_demo.cmd)
