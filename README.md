# 異体字正規化モジュール
　「髙（はしご高）」「﨑（立つ崎）」などの異体字を、標準文字（JIS文字集合に含まれる文字）へと変換します。

## 導入方法
```shell
$ pip install ja-cvu-normalizer
```

## 利用例
```python
from ja_cvu_normalizer.ja_cvu_normalizer import JaCvuNormalizer
text = "髙橋"
ja_cvu_normalizer = JaCvuNormalizer()
print(ja_cvu_normalizer.normalize(text))
# -> 高橋
```

## 謝辞
- `resource/ISO-2022-JP.txt`は[異字体変換テーブル](https://github.com/AnaKutsu/character_variants_unicode_to_jis)のリポジトリから拝借させていただきました。
