ENGLISH ===================

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

日本語 ===================

以下のREADMEはAIによって翻訳されています。もし不明な点がありましたら、お詫び申し上げます。

このプログラムは、colmsgファイルを表示するためのHTMLファイルを作成します。

例えば、colmsgファイルを以下のフォルダーに保存した場合：
C:\Prog\colmsg\data\日木坂26\白石七瀬
C:\Prog\colmsg\data\日木坂26\加藤京子

そして、HTMLファイルを以下のフォルダーに作成したい場合：
C:\Prog\colmsg\html\日木坂26

次に、コマンドラインでプログラムを実行します：
colmsg_html "C:\Prog\colmsg\data\日木坂26" "C:\Prog\colmsg\html\日木坂26"

その後、以下のフォルダーに月ごとのHTMLファイルが作成されます：
C:\Prog\colmsg\html\日木坂26\日木坂26-白石七瀬\日木坂26-白石七瀬YYYYMM.html
C:\Prog\colmsg\html\日木坂26\日木坂26-加藤京子\日木坂26-加藤京子YYYYMM.html

コマンドの最後にニックネームを付けることもできます。そうしない場合は「としくん」がデフォルトで使用されます。

スクリプトでプログラムを実行したい場合は、Unicode文字を認識するために「chcp 65001」を追加することを忘れないでください。（run_demo.cmdを参照）
