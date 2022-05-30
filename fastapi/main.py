# FastAPIインポート
from fastapi import FastAPI
# 型ヒントを行えるpydanticをインポート
from pydantic import BaseModel  

# 作成したモデル定義ファイルと設定ファイルをインポート
import db_model as m 
import db_setting as s 

# データクラス定義
# POSTとPUTで使うデータクラス
class UserBase(BaseModel):
    name : str
    mail : str
    sex : str

# FastAPIのインスタンス作成
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# GETメソッドで /usersにアクセスしたときの処理
# ユーザーの全件取得
@app.get("/users", tags=["users"])
async def read_users():
    #DBからユーザ情報を取得
    result = s.session.query(m.Users).all()
    return result
