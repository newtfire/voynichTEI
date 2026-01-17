import re
import requests

# Make it accept web text files
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/plain, */*"
}

# Getting the README Information about the Transliteration file
try:
    # 2. Pass the headers argument to the get function
    response = requests.get("https://www.voynich.nu/data/000_README.txt", headers=headers)
    response.raise_for_status()
    full_text = response.text
    relevant_content = full_text.split("ZL3a-n.txt", 1)[1] # Get everything after ZL3a-n.txt

except requests.exceptions.RequestException as e:
    print(f"Error fetching the file: {e}")

# Read the Transliteration file
with open('../transliterationFiles/ZL3b-n/ZL3b-n.txt', 'r', encoding='utf-8') as file:
    filedata = file.read()

# Define all replacements in a dictionary (Target : Replacement)
replacements = {
    '@128;': '€',
    '@130;': '‚',
    '@131;': 'ƒ',
    '@132;': '„',
    '@133;': '…',
    '@134;': '†',
    '@135;': '‡',
    '@136;': 'ˆ',
    '@137;': '‰',
    '@138;': 'Š',
    '@139;': '‹',
    '@140;': 'Œ',
    '@142;': 'Ž',
    '@145;': "‘",
    '@146;': "’",
    '@147;': '“',
    '@148;': '”',
    '@149;': '•',
    '@150;': '–',
    '@151;': '—',
    '@152;': '˜',
    '@153;': '™',
    '@154;': 'š',
    '@155;': '›',
    '@156;': 'œ',
    '@158;': 'ž',
    '@159;': 'Ÿ',
    '@160;': ' ',
    '@161;': '¡',
    '@162;': '¢',
    '@163;': '£',
    '@164;': '¤',
    '@165;': '¥',
    '@166;': '¦',
    '@167;': '§',
    '@168;': '¨',
    '@169;': '©',
    '@170;': 'ª',
    '@171;': '«',
    '@172;': '¬',
    '@173;': '­',
    '@174;': '®',
    '@175;': '¯',
    '@176;': '°',
    '@177;': '±',
    '@178;': '²',
    '@179;': '³',
    '@180;': '´',
    '@181;': 'μ',
    '@182;': '¶',
    '@183;': '·',
    '@184;': '¸',
    '@185;': '¹',
    '@186;': 'º',
    '@187;': '»',
    '@188;': '¼',
    '@189;': '½',
    '@190;': '¾',
    '@191;': '¿',
    '@192;': 'À',
    '@193;': 'Á',
    '@194;': 'Â',
    '@195;': 'Ã',
    '@196;': 'Ä',
    '@197;': 'Å',
    '@198;': 'Æ',
    '@199;': 'Ç',
    '@200;': 'È',
    '@201;': 'É',
    '@202;': 'Ê',
    '@203;': 'Ë',
    '@204;': 'Ì',
    '@205;': 'Í',
    '@206;': 'Î',
    '@207;': 'Ï',
    '@208;': 'Ð',
    '@209;': 'Ñ',
    '@210;': 'Ò',
    '@211;': 'Ó',
    '@212;': 'Ô',
    '@213;': 'Õ',
    '@214;': 'Ö',
    '@215;': '×',
    '@216;': 'Ø',
    '@217;': 'Ù',
    '@218;': 'Ú',
    '@219;': 'Û',
    '@220;': 'Ü',
    '@221;': 'Ý',
    '@222;': 'Þ',
    '@223;': 'ß',
    '@224;': 'à',
    '@225;': 'á',
    '@226;': 'â',
    '@227;': 'ã',
    '@228;': 'ä',
    '@229;': 'å',
    '@230;': 'æ',
    '@231;': 'ç',
    '@232;': 'è',
    '@233;': 'é',
    '@234;': 'ê',
    '@235;': 'ë',
    '@236;': 'ì',
    '@237;': 'í',
    '@238;': 'î',
    '@239;': 'ï',
    '@240;': 'ð',
    '@241;': 'ñ',
    '@242;': 'ò',
    '@243;': 'ó',
    '@244;': 'ô',
    '@245;': 'õ',
    '@246;': 'ö',
    '@252;': 'ü',
    '@253;': 'ý',
    '@254;': 'þ',
    '@255;': 'ÿ'
}

# 1. Apply the Dictionary Replacements Loop
for code, char in replacements.items():
    filedata = filedata.replace(code, char)

# 2. Apply the Regex Replacement (using re.sub instead of replace)
# Looks for patterns like <f76r> and converts to TEI surface tags
filedata = re.sub(r'<(f\d\d?\d?[rv]?\d?)>', r'</surface><surface n="\1">', filedata)
filedata = re.sub(r'(<.+>)(\s+)(<%>)', r'\3\1\2', filedata)
filedata = re.sub(r'<%>', '<zone>', filedata)
filedata = re.sub(r'<\$>', '</zone>', filedata)
filedata = re.sub(r'<->', '<figure/>', filedata)
filedata = re.sub(r'<~>', '<figure/>', filedata)

# Write the file out again
with open('../transliterationFiles/ZL3b-n/ZL3b-n_test.txt', 'w', encoding='utf-8') as file:
    file.write(relevant_content.strip()) # Gets Info from website ReadMe
    file.write(filedata) # Changed File

print("Conversion complete.")