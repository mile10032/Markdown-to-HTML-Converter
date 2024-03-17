import markdown
import os
import sys
#バリデーション
def inputCheck(path):

    validateList = ["<", ">", ":", '"', "\\", "|", "?", "*"]

    if path == "":
        return False
    osName = os.name

    if osName == "posix":
        for char in path:
            if char in validateList:
                print("無効な文字が入っています。")
                return False
            
    elif osName == "nt":
        tempList = validateList.copy()
        tempList.remove(":")
        for char in path:
            if char in tempList:
                print("無効な文字が入っています。")
                return False
    else:
        print("未知のOSが使われています。システムの対応外です。")
        return False
    
    if path.startswith("/") or path.startswith(".") or (len(path) > 1 and path[1] == ":" and path[0].isalpha()):
        return True
    else:
        print("パスの形式が不正です。")
        return False

def Markdown(inputpath, outputpath):

    if not inputCheck(outputpath):
        sys.exit("出力パスを正しいものに変えてやり直してください。")

    if not inputCheck(inputpath) or not inputpath[-3:].lower() == ".md":
        sys.exit("入力パスを正しいものに変えてやり直してください。")
    
    print('対象のファイルがあるか検索します。')

    if os.path.exists(inputpath):
        with open(inputpath, 'r') as f:
            fileContent = f.read()
            print("ファイルが見つかりました。")
    else:
        sys.exit("ファイルがありませんでした、終了します。")

    #マークダウンをHTMLに変換
    html = markdown.markdown(fileContent)
    with open(outputpath, 'w') as f2:
        f2.write(html)
    print("変換が完了しました。")

#sys.aegvで入力を受け取る
#コードブロックを定義   
if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1].lower() != "markdown":
        sys.exit("正しいコマンドを入力してください。例)python script.py markdown input.md output.html")
    else:
        Markdown(sys.argv[2], sys.argv[3])

print("finish!!")
