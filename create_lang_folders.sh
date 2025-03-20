#!/bin/bash

# 定义语言代码列表
languages=("zh-Hans" "zh-Hant" "ar" "sq" "am" "ar-001" "hy" "bs" "bg" "my-MM"
           "ca" "hr" "cs" "da" "nl" "et" "fi" "fr" "ka" "de" "el" "gu" "hi" "hu"
           "is" "id" "it" "ja" "kn" "kk" "ko" "lv" "lt" "mk" "nb" "ms" "ml" "mr"
           "mn" "fa" "pl" "pt-PT" "pa" "ro" "ru" "sr" "sk" "sl" "pau" "so" "es"
           "sw" "sv" "ta" "te" "th" "tr" "uk" "ur" "vi")

# 遍历数组，创建文件夹，并在其中创建 privacy-policy.md
for lang in "${languages[@]}"; do
    mkdir -p "$lang"  # 创建文件夹
    touch "$lang/privacy-policy.md"  # 在文件夹内创建空文件
    echo "Created folder: $lang and privacy-policy.md"
done

echo "✅ All language folders and privacy-policy.md files have been created!"

