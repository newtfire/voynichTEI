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

titleStmt = ""
try:
    with open('../xml/header/titleStmt.xml', 'r', encoding='utf-8') as ts_file:
        titleStmt = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/titleStmt.xml' was not found.")
except Exception as e:
    print(f"Error reading titleStmt.xml: {e}")

# 2. publicationStmt (This one was correct)
publicationStmt = ""
try:
    with open('../xml/header/publicationStmt.xml', 'r', encoding='utf-8') as ts_file:
        publicationStmt = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/publicationStmt.xml' was not found.")
except Exception as e:
    print(f"Error reading publicationStmt.xml: {e}")

# 3. msIdentifier (FIXED: Assign to msIdentifier, not publicationStmt)
msIdentifier = ""
try:
    with open('../xml/header/msIdentifier.xml', 'r', encoding='utf-8') as ts_file:
        msIdentifier = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/msIdentifier.xml' was not found.")
except Exception as e:
    print(f"Error reading msIdentifier.xml: {e}")

# 4. handDesc (FIXED)
handDesc = ""
try:
    with open('../xml/header/handDesc.xml', 'r', encoding='utf-8') as ts_file:
        handDesc = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/handDesc.xml' was not found.")
except Exception as e:
    print(f"Error reading handDesc.xml: {e}")

# 5. bindingDesc (FIXED)
bindingDesc = ""
try:
    with open('../xml/header/bindingDesc.xml', 'r', encoding='utf-8') as ts_file:
        bindingDesc = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/bindingDesc.xml' was not found.")
except Exception as e:
    print(f"Error reading bindingDesc.xml: {e}")

# 6. history (FIXED)
history = ""
try:
    with open('../xml/header/history.xml', 'r', encoding='utf-8') as ts_file:
        history = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/history.xml' was not found.")
except Exception as e:
    print(f"Error reading history.xml: {e}")

# 7. tagsDecl (FIXED)
tagsDecl = ""
try:
    with open('../xml/header/tagsDecl.xml', 'r', encoding='utf-8') as ts_file:
        tagsDecl = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/tagsDecl.xml' was not found.")
except Exception as e:
    print(f"Error reading tagsDecl.xml: {e}")

# 8. langUsage (FIXED)
langUsage = ""
try:
    with open('../xml/header/langUsage.xml', 'r', encoding='utf-8') as ts_file:
        langUsage = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/langUsage.xml' was not found.")
except Exception as e:
    print(f"Error reading langUsage.xml: {e}")




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
    '@255;': 'ÿ',
    '<': '&lt;',
    '>': '&gt;',
    '#': '<note type="outline">',
    '&lt;!': '<note type="inline">',
    '&lt;unreadable&gt;': '<unclear/>'
}

# 1. Apply the Dictionary Replacements Loop
for code, char in replacements.items():
    filedata = filedata.replace(code, char)

# End Comments
filedata = re.sub(r'<note type="outline">(.+?)&gt;', r'<note type="outline">\1</note>', filedata)
filedata = re.sub(r'<note type="inline">(.+?)&gt;', r'<note type="inline">\1</note>', filedata)
# Looks for patterns like <f76r> and converts to TEI surface tags
filedata = re.sub(r'&lt;(f\d\d?\d?[rv]?\d?)&gt;', r'</surface><surface n="\1">', filedata)
filedata = re.sub(r'(&lt;.+&gt;)(\s+)(<note type="inline">[A-Z]</note>)(<%>)', r'\4\1\3', filedata)
filedata = re.sub(r'(&lt;.+&gt;)(\s+)(&lt;%&gt;)', r'\3\1\2', filedata)
# Zones
filedata = re.sub(r'&lt;%&gt;', '<zone>', filedata)
filedata = re.sub(r'&lt;\$&gt;', '</zone>', filedata)
# Figures
filedata = re.sub(r'&lt;-&gt;', '<figure/>', filedata)
filedata = re.sub(r'&lt;~&gt;', '<figure/>', filedata)
# Lines
filedata = re.sub(r'&lt;f\d+[rv]\d?\.(\d+),([@+*=&~/!])([PLCR][01bcrtafnpstxzio])&gt;\s+(.+)', r'<line n="\1" rendition="#\2 #\3">\4</line>', filedata)
filedata = re.sub(r'&lt;fRos\.(\d+),([@+*=&~/!])([PLCR][01bcrtafnpstxzio])&gt;\s+(.+)', r'<line n="\1" rendition="#\2 #\3">\4</line>', filedata)
# Fixing Zones
filedata = re.sub(r'(</zone>)(</line>)', r'\2\1', filedata)
# Locator Char
filedata = re.sub(r'rendition="#@', r'rendition="#At', filedata)
filedata = re.sub(r'rendition="#\+', r'rendition="#Ad', filedata)
filedata = re.sub(r'rendition="#\*', r'rendition="#As', filedata)
filedata = re.sub(r'rendition="#=', r'rendition="#Aq', filedata)
filedata = re.sub(r'rendition="#&', r'rendition="#An', filedata)
filedata = re.sub(r'rendition="#~', r'rendition="#Am', filedata)
filedata = re.sub(r'rendition="#/', r'rendition="#Al', filedata)
filedata = re.sub(r'rendition="#!', r'rendition="#Ax', filedata)
# Label Elements
filedata = re.sub(r'<note type="outline"> page (\d+)', r'<label>PAGE \1</label>', filedata)
filedata = re.sub(r'(<label>PAGE \d+)(</label>)(,)\s?(\d+)', r'\1\3 \4\2', filedata)
filedata = re.sub(r'<note type="outline"> astronomical', r'<label>ASTRONOMICAL</label>', filedata)
filedata = re.sub(r'<note type="outline"> biological', r'<label>BIOLOGICAL</label>', filedata)
filedata = re.sub(r'<note type="outline"> cosmological', r'<label>COSMOLOGICAL</label>', filedata)
filedata = re.sub(r'<note type="outline"> herbal', r'<label>HERBAL</label>', filedata)
filedata = re.sub(r'<note type="outline"> pharmaceutical', r'<label>PHARMACEUTICAL</label>', filedata)
filedata = re.sub(r'<note type="outline"> text only', r'<label>TEXT ONLY</label>', filedata)
filedata = re.sub(r'<label>TEXT ONLY</label>\s+?/ stars', r'<label>TEXT ONLY / STARS</label>', filedata)
filedata = re.sub(r'<label>TEXT ONLY</label>/ stars', r'<label>TEXT ONLY / STARS</label>', filedata)
filedata = re.sub(r'<note type="outline"> Pisces', r'<label>PISCES</label>', filedata)
filedata = re.sub(r'<note type="outline"> Aries \(dark\)', r'<label>ARIES (DARK)</label>', filedata)
filedata = re.sub(r'<note type="outline"> Aries \(light\)', r'<label>ARIES (LIGHT)</label>', filedata)
filedata = re.sub(r'<note type="outline"> Taurus \(dark\)', r'<label>TAURUS (DARK)</label>', filedata)
filedata = re.sub(r'<note type="outline"> Taurus \(light\)', r'<label>TAURUS (LIGHT)</label>', filedata)
filedata = re.sub(r'<note type="outline"> Gemini', r'<label>GEMINI</label>', filedata)
filedata = re.sub(r'<note type="outline"> Cancer', r'<label>CANCER</label>', filedata)
filedata = re.sub(r'<note type="outline"> Leo(\s+)', r'<label>LEO</label>\1', filedata)
filedata = re.sub(r'<note type="outline"> Virgo', r'<label>VIRGO</label>', filedata)
filedata = re.sub(r'<note type="outline"> Libra', r'<label>LIBRA</label>', filedata)
filedata = re.sub(r'<note type="outline"> Scorpius', r'<label>SCORPIUS</label>', filedata)
filedata = re.sub(r'<note type="outline"> Sagittarius', r'<label>SAGITTARIUS</label>', filedata)
# Comments Again
filedata = re.sub(r'(<note type="outline">)(.+)', r'\1\2</note>', filedata)
filedata = re.sub(r'(<note type="outline">)(\n)', r'\2', filedata)
# Lines Again
filedata = re.sub(r'&lt;f\d+[rv]\d?\.(\d+),@(Pb)>(.+)', r'<line n="\1" rendition="#At #\2">\3</line>', filedata)
filedata = re.sub(r'(<line n="\d+" rendition="#[A-Z][a-z] #[A-Z][a-z]">)(<note type="outline">.+</note>)(<zone>)', r'\3\1\2', filedata)
filedata = re.sub(r'(<line n="\d+" rendition="#[A-Z][a-z] #[A-Z][a-z]">)(<note type="inline">.+</note>)(<zone>)', r'\3\1\2', filedata)
# Fixing fRos
filedata = re.sub(r'&lt;(fRos)&gt;', r'</surface><surface n="\1">', filedata)
filedata = re.sub(r'(<zone)(><line n="\d\d?" rendition="#A[td] #P0">)<@H=(\d)>', r'\1 hand="#scribe\3"\2', filedata)
# Fixing Specific Comments
filedata = re.sub(r'(<note type="outline"> Plant ID: <unclear/)</note>(, Fern, Maidenhair fern\?\?\? Tansy\?</note>)', r'\1>\2', filedata)
filedata = re.sub(r'(<note type="outline"> has extraneous writing ==)</note>( Saturn symbol in lower right corner</note>)', r'\1>\2', filedata)
filedata = re.sub(r'(<note type="outline"> eva in &lt; )</note>(, approximately:</note>)', r'\1&gt;\2', filedata)
filedata = re.sub(r'(<note type="outline"> \+ nuchicon oladab&lt;yd)</note> (\+ multo&lt;d&gt; \+ tc \+ c&lt;h&gt;vc \+ porta&lt;d&gt; \+ n \+)', r'\1&gt;\2', filedata)
filedata = re.sub(r'(<note type="outline"> &lt;f101r2)</note>       (\{\$I=P \$Q=S \$P=F}</note>)',r'\1&gt;\2', filedata)

# Write the file out again
with open('../transliterationFiles/ZL3b-n/ZL3b-n_test.xml', 'w', encoding='utf-8') as file:
    file.write('<?xml version="1.0" encoding="UTF-8"?>')
    file.write('<?xml-stylesheet type="text/css" href="evaFontCSS.css"?>')
    file.write('<?xml-model href="https://tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>')
    file.write('<TEI xmlns="http://www.tei-c.org/ns/1.0">')
    file.write("<teiHeader>") # Start of Header
    file.write("<fileDesc>")  # Start of fileStmt
    file.write(titleStmt)
    file.write(publicationStmt)
    file.write("<sourceDesc>")
    file.write("<msDesc>")
    file.write(msIdentifier)
    file.write("<physDesc>")
    file.write(handDesc)
    file.write(bindingDesc)
    file.write("</physDesc>")
    file.write(history)
    file.write("<msContents>")
    file.write("<summary>")
    file.write(relevant_content.strip()) # Gets Info from website ReadMe
    file.write("</summary>")
    file.write("</msContents>")
    file.write("</msDesc>")
    file.write("</sourceDesc>")
    file.write("</fileDesc>")
    file.write("<encodingDesc>")
    file.write(tagsDecl)
    file.write("</encodingDesc>")
    file.write("<profileDesc>")
    file.write(langUsage)
    file.write("</profileDesc>")
    file.write("</teiHeader>")
    file.write("<sourceDoc>")
    file.write(filedata) # Changed File
    file.write("</surface>")
    file.write("</sourceDoc>")
    file.write("</TEI>")

print("Conversion complete.")