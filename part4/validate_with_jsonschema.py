from jsonschema import validate # pip install jsonschema

# 次の4つのルールを持つスキーマ(期待するデータ構造)を定義する

schema = {
    "type": "object", # ルール1: 値はJSONに置けるオブジェクト(pythoにおけるdict)である
    "properties" : {
        # ルール2: name の値は文字列である。
        "name": {
            "type": "string"
        },
        # ルール3: priceの値は文字列で、patternに指定した正規表現にマッチする。
        "price": {
            "type": "string",
            "pattern": "^[0-9,]+$"
        }
    },
    "required": ["name", "price"] # ルール4: dictのキーととpriceは必須である
}

# validate()関数は、第一引数のオブジェクトを第二引数のスキーマでバリデーションする。
validate({
    'name': 'ぶどう',
    'price': '3,000',
}, schema) # スキーマに適合するので例外は発生しない。

validate({
    'name': 'みかん',
    'price': '無料'
}, schema)