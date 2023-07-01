CharaVoiceChanger(BGMLoaderを改変して作成)

必要プラグイン
BepInEx v5.4.4以降
SB3UGSもしくはUnityStudio

インストール方法
BGMLoader.dllを入れ替えて
Koikatu\BepInEx\pluginに各フォルダを作成してください。

元々の機能を残しつつ
キャラクターの声を好きな声に差し替えるmodです。
ただ量が量なので作成には根気が必要

使い方
voiceフォルダ内の各キャラフォルダに対応する声をwav形式またはogg形式で入れる
(コンフィグで選択式)

曲名はSB3UGSもしくはUnityStudioで確認して次のように名前を付ける
(確認するunity3dは
abdata\h\list\00_00
abdata\h\list\20_00
abdata\h\list\54_00 55_00 56_00
一応テキストデータを出力しましたが見づらいかも)


例　h_ka_01_01_023 →　ka01023.wav

h_ka_zz_xx_yyy    →　	kaxxyyy.wav	kaxxyyy.ogg
h_ai_zz_xx_yyy    →　	aixxyyy.wav	aixxyyy.ogg
h_hh_zz_xx_yyy    →　	hhxxyyy.wav	hhxxyyy.ogg
h_so_zz_xx_yyy    →　	soxxyyy.wav	soxxyyy.ogg
h_on_zz_xx_yyy    →　	onxxyyy.wav	onxxyyy.ogg
h_ko_zz_xx_yyy    →　	koxxyyy.wav	koxxyyy.ogg
h_ko_zz_xx_yyy_aa →　	koxxyyyaa.wav	koxxyyyaa.ogg
h_fe_zz_xx_yyy 	  →　	fexxyyy.wav	fexxyyy.ogg
h_ka3p_zz_xx_yyy  →　	ka3pxxyyy.wav  	ka3pxxyyy.ogg
h_hh3p_zz_xx_yyy  →　	hh3pxxyyy.wav  	hh3pxxyyy.ogg
h_so3p_zz_xx_yyy  →　	so3pxxyyy.wav  	so3pxxyyy.ogg
h_ka_dk_zz_00_yyy →　	kadkyyy.wav  	kadkyyy.ogg
h_hh_dk_zz_00_yyy →　	hhdkyyy.wav  	hhdkyyy.ogg
h_so_dk_zz_00_yyy →　	sodkyyy.wav  	sodkyyy.ogg
h_ko_dk_zz_00_yyy →　	kodkyyy.wav  	kodkyyy.ogg
h_ko_dk_zz_00_yyy_aa → kodkyyyaa.wav  	kodkyyyaa.ogg

xxの値は基本的に
00=初めて　01=不慣れ　02=慣れ　03=淫乱

(淫乱のH開始ボイスはka03000.wav ka03001.wav ka03002.wav)

zzの値は性格番号

存在しない数値を入力するとロード時間に支障をきたす可能性あり


・愛称
namelist_sp_zz_xx_yyy →　namexxyyy.wav  namexxyyy.ogg

xxの値はイントネーションの違いで00、01、02の三パターン

yyyの値は
000=先輩　001=お兄ちゃん　002=先生　003=ダーリン　004=ご主人様

・効果音
SEフォルダにwav形式で入れる
systemse（クリック時の音）とse/hフォルダ（挿入音等）を差し替え可
差し替え可能な音は対応表に
xxx →  xxx.wav
(アンダーバーも入力)

・BGM
BGMフォルダにogg形式で入れる
bgm_xx → bgmxx.ogg

・タイトルコール
Introclipsフォルダbrandcallフォルダそれぞれにwav形式で入れる
ランダムで再生される


更新履歴
2021/04/15	・後半のキャラが機能しないバグを修正
		・Hリザルトシーンで発生するエラーの修正
		・元のBGMLoader.dllが残っていると使用できないように

2020/12/13	・BepInExv5.4.4以降用に更新

2020/11/11	・キャラスタジオでBGMが再生できない問題を修正

2020/11/08	・キャラスタジオに対応

2020/07/27	・LogOutputのDebugメッセージを修正
		・コンフィグからvoiceをwavかoggを選べるように変更

2020/04/13	・LogOutputにエラーログが出ていたのを修正

2020/04/12	・shortbreath（タッチ時の音声）に対応
		・systemse及びse/hに対応

2020/03/22	・BepInEx4版をリリース

2020/03/19	・yyyの値の百の位が機能していないバグを修正しました。
		・AS追加ボイスに漏れがあったので追加
		・愛称（特殊）を差し替えられるように
		・ogg形式版を同梱、どちらか選択して導入してください。
		　選択できるのはvoiceデータのみ、他はそのまま

2020/03/16	・全性格に対応しました。
		・吐息を差し替えられるように

2020/03/14	・ブランドコールとタイトルコールのフォルダを分割しました。
		　タイトルコールはIntroclipsフォルダに
		　ブランドコールはbrandcallフォルダに入れてください。
		・対応表を追加しました。
		
2020/03/14	・最初のバージョン




