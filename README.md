# 異体字正規化モジュール
　「髙（はしご高）」「﨑（立つ崎）」などの異体字を、標準文字（JIS文字集合に含まれる文字）へと変換します。

## 導入方法
- 準備中

## 利用例
```python
from jp_cvu_normalizer.jp_cvu_normalizer import JpCvuNormalizer
text = "髙橋"
jp_cvu_normalizer = JpCvuNormalizer()
print(jp_cvu_normalizer.normalize(text))
# -> 高橋
```

## 謝辞
- `resource/ISO-2022-JP.txt`は[異字体変換テーブル](https://github.com/AnaKutsu/character_variants_unicode_to_jis)のリポジトリから拝借させていただきました。
