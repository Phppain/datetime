"""task10.py"""

RU_TO_EN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ь': '',
    'Ы': 'Y', 'Ъ': '', 'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ь': '',
    'ы': 'y', 'ъ': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}

EN_TO_RU = {v: k for k, v in RU_TO_EN.items()}

def transliterate(text, direction):
    if direction == 'ru_to_en':
        translation_map = RU_TO_EN
    elif direction == 'en_to_ru':
        translation_map = EN_TO_RU
    else:
        raise ValueError("Invalid direction. Use 'ru_to_en' or 'en_to_ru'.")
    
    return ''.join(translation_map.get(char, char) for char in text)

def transliterate_file(input_file, output_file, direction):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    translated_text = transliterate(text, direction)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)

if __name__ == "__main__":
    direction = input("Введите направление (ru_to_en/en_to_ru): ")
    transliterate_file('input.txt', 'output.txt', direction)
