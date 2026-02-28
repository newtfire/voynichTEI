import re
import requests

# Make it accept web text files
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/plain, */*"
}

try:
    response = requests.get("https://www.voynich.nu/data/000_README.txt", headers=headers)
    response.raise_for_status()
    full_text = response.text
    delimiter = "ZL3a-n.txt"
    if delimiter in full_text:
        # Split by the name, then strip away the dashed line manually
        relevant_content = full_text.split(delimiter, 1)[1].strip()
        # Remove the dashes if they are still at the start
        relevant_content = re.sub(r'^-+\s+', '', relevant_content)
    else:
        relevant_content = "Content not found."

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

publicationStmt = ""
try:
    with open('../xml/header/publicationStmt.xml', 'r', encoding='utf-8') as ts_file:
        publicationStmt = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/publicationStmt.xml' was not found.")
except Exception as e:
    print(f"Error reading publicationStmt.xml: {e}")

msIdentifier = ""
try:
    with open('../xml/header/msIdentifier.xml', 'r', encoding='utf-8') as ts_file:
        msIdentifier = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/msIdentifier.xml' was not found.")
except Exception as e:
    print(f"Error reading msIdentifier.xml: {e}")

handDesc = ""
try:
    with open('../xml/header/handDesc.xml', 'r', encoding='utf-8') as ts_file:
        handDesc = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/handDesc.xml' was not found.")
except Exception as e:
    print(f"Error reading handDesc.xml: {e}")

bindingDesc = ""
try:
    with open('../xml/header/bindingDesc.xml', 'r', encoding='utf-8') as ts_file:
        bindingDesc = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/bindingDesc.xml' was not found.")
except Exception as e:
    print(f"Error reading bindingDesc.xml: {e}")

history = ""
try:
    with open('../xml/header/history.xml', 'r', encoding='utf-8') as ts_file:
        history = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/history.xml' was not found.")
except Exception as e:
    print(f"Error reading history.xml: {e}")

charDecl = ""
try:
    with open('../xml/header/charDecl.xml', 'r', encoding='utf-8') as ts_file:
        charDecl = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/charDecl.xml' was not found.")
except Exception as e:
    print(f"Error reading charDecl.xml: {e}")

tagsDecl = ""
try:
    with open('../xml/header/tagsDecl.xml', 'r', encoding='utf-8') as ts_file:
        tagsDecl = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/tagsDecl.xml' was not found.")
except Exception as e:
    print(f"Error reading tagsDecl.xml: {e}")


langUsage = ""
try:
    with open('../xml/header/langUsage.xml', 'r', encoding='utf-8') as ts_file:
        langUsage = ts_file.read()
except FileNotFoundError:
    print("Warning: '../xml/header/langUsage.xml' was not found.")
except Exception as e:
    print(f"Error reading langUsage.xml: {e}")


with open('../ixml/ixml.xml', 'r', encoding='utf-8') as file:
    filedata = file.read()

replacements = {

#    '€': '<g ref="#u20ac">€</g>',
#    '‚': '<g ref="#u201a">‚</g>',
#    'ƒ': '<g ref="#u0192">ƒ</g>',
#    '„': '<g ref="#u201e">„</g>',
#    '…': '<g ref="#u2026">…</g>',
#    '†': '<g ref="#u2020">†</g>',
#    '‡': '<g ref="#u2021">‡</g>',
#    'ˆ': '<g ref="#u02c6">ˆ</g>',
#    '‰': '<g ref="#u2030">‰</g>',
#    'Š': '<g ref="#u0160">Š</g>',
#    '‹': '<g ref="#u2039">‹</g>',
#    'Œ': '<g ref="#u0152">Œ</g>',
#    'Ž': '<g ref="#u017d">Ž</g>',
#    '‘': '<g ref="#u2018">‘</g>',
#    '’': '<g ref="#u2019">’</g>',
#    '“': '<g ref="#u201c">“</g>',
#    '”': '<g ref="#u201d">”</g>',
#    '•': '<g ref="#u2022">•</g>',
#    '–': '<g ref="#u2013">–</g>',
#    '—': '<g ref="#u2014">—</g>',
#    '˜': '<g ref="#u02dc">˜</g>',
#    '™': '<g ref="#u2122">™</g>',
#    'š': '<g ref="#u0161">š</g>',
#    '›': '<g ref="#u203a">›</g>',
#    'œ': '<g ref="#u0153">œ</g>',
#   'ž': '<g ref="#u017e">ž</g>',
#    'Ÿ': '<g ref="#u0178">Ÿ</g>',
#    ' ': '<g ref="#u0020"> </g>',
#    '¡': '<g ref="#u00a1">¡</g>',
#    '¢': '<g ref="#u00a2">¢</g>',
#    '£': '<g ref="#u00a3">£</g>',
#    '¤': '<g ref="#u00a4">¤</g>',
#    '¥': '<g ref="#u00a5">¥</g>',
#    '¦': '<g ref="#u00a6">¦</g>',
#    '§': '<g ref="#u00a7">§</g>',
#    '¨': '<g ref="#u00a8">¨</g>',
#    '©': '<g ref="#u00a9">©</g>',
#    'ª': '<g ref="#u00aa">ª</g>',
#    '«': '<g ref="#u00ab">«</g>',
#    '¬': '<g ref="#u00ac">¬</g>',
#    '­': '<g ref="#u00ad">­</g>',
#    '®': '<g ref="#u00ae">®</g>',
#    '¯': '<g ref="#u00af">¯</g>',
#    '°': '<g ref="#u00b0">°</g>',
#    '±': '<g ref="#u00b1">±</g>',
#    '²': '<g ref="#u00b2">²</g>',
#    '³': '<g ref="#u00b3">³</g>',
#    '´': '<g ref="#u00b4">´</g>',
#    'μ': '<g ref="#u03bc">μ</g>',
#    '¶': '<g ref="#u00b6">¶</g>',
#    '·': '<g ref="#u00b7">·</g>',
#    '¸': '<g ref="#u00b8">¸</g>',
#    '¹': '<g ref="#u00b9">¹</g>',
#    'º': '<g ref="#u00ba">º</g>',
#    '»': '<g ref="#u00bb">»</g>',
#    '¼': '<g ref="#u00bc">¼</g>',
#    '½': '<g ref="#u00bd">½</g>',
#    '¾': '<g ref="#u00be">¾</g>',
#    '¿': '<g ref="#u00bf">¿</g>',
#    'À': '<g ref="#u00c0">À</g>',
#    'Á': '<g ref="#u00c1">Á</g>',
#    'Â': '<g ref="#u00c2">Â</g>',
#    'Ã': '<g ref="#u00c3">Ã</g>',
#    'Ä': '<g ref="#u00c4">Ä</g>',
#    'Å': '<g ref="#u00c5">Å</g>',
#    'Æ': '<g ref="#u00c6">Æ</g>',
#    'Ç': '<g ref="#u00c7">Ç</g>',
#    'È': '<g ref="#u00c8">È</g>',
#    'É': '<g ref="#u00c9">É</g>',
#    'Ê': '<g ref="#u00ca">Ê</g>',
#    'Ë': '<g ref="#u00cb">Ë</g>',
#    'Ì': '<g ref="#u00cc">Ì</g>',
#    'Í': '<g ref="#u00cd">Í</g>',
#    'Î': '<g ref="#u00ce">Î</g>',
#    'Ï': '<g ref="#u00cf">Ï</g>',
#    'Ð': '<g ref="#u00d0">Ð</g>',
#    'Ñ': '<g ref="#u00d1">Ñ</g>',
#    'Ò': '<g ref="#u00d2">Ò</g>',
#    'Ó': '<g ref="#u00d3">Ó</g>',
#    'Ô': '<g ref="#u00d4">Ô</g>',
#    'Õ': '<g ref="#u00d5">Õ</g>',
#    'Ö': '<g ref="#u00d6">Ö</g>',
#    '×': '<g ref="#u00d7">×</g>',
#    'Ø': '<g ref="#u00d8">Ø</g>',
#    'Ù': '<g ref="#u00d9">Ù</g>',
#    'Ú': '<g ref="#u00da">Ú</g>',
#    'Û': '<g ref="#u00db">Û</g>',
#    'Ü': '<g ref="#u00dc">Ü</g>',
#    'Ý': '<g ref="#u00dd">Ý</g>',
#    'Þ': '<g ref="#u00de">Þ</g>',
#    'ß': '<g ref="#u00df">ß</g>',
#    'à': '<g ref="#u00e0">à</g>',
#    'á': '<g ref="#u00e1">á</g>',
#    'â': '<g ref="#u00e2">â</g>',
#    'ã': '<g ref="#u00e3">ã</g>',
#    'ä': '<g ref="#u00e4">ä</g>',
#    'å': '<g ref="#u00e5">å</g>',
#    'æ': '<g ref="#u00e6">æ</g>',
#    'ç': '<g ref="#u00e7">ç</g>',
#    'è': '<g ref="#u00e8">è</g>',
#    'é': '<g ref="#u00e9">é</g>',
#    'ê': '<g ref="#u00ea">ê</g>',
#    'ë': '<g ref="#u00eb">ë</g>',
#    'ì': '<g ref="#u00ec">ì</g>',
#    'í': '<g ref="#u00ed">í</g>',
#    'î': '<g ref="#u00ee">î</g>',
#    'ï': '<g ref="#u00ef">ï</g>',
#    'ð': '<g ref="#u00f0">ð</g>',
#    'ñ': '<g ref="#u00f1">ñ</g>',
#    'ò': '<g ref="#u00f2">ò</g>',
#    'ó': '<g ref="#u00f3">ó</g>',
#    'ô': '<g ref="#u00f4">ô</g>',
#    'õ': '<g ref="#u00f5">õ</g>',
#    'ö': '<g ref="#u00f6">ö</g>',
#    'ü': '<g ref="#u00fc">ü</g>',
#    'ý': '<g ref="#u00fd">ý</g>',
#    'þ': '<g ref="#u00fe">þ</g>',
#    'ÿ': '<g ref="#u00ff">ÿ</g>',

    'lineN': 'n',
    'surfaceN': 'n',
    '<unclearAlt>': '<unclear>',
    '</unclearAlt>': '</unclear>',
    '<comment>': '<note type="comment">',
    '</comment>': '</note>'
}

for code, char in replacements.items():
    filedata = filedata.replace(code, char)

filedata = re.sub(r'"\n\s+>', r'">', filedata)
filedata = re.sub(r'(<line n="\d+" rendition="[@+*=&~/!][PLCR][01bcrtafnpstxzio]">)(<startPara/>)', r'<zone>\1', filedata)
filedata = re.sub(r'<endPara/>(</line>)', r'\1</zone>', filedata)
filedata = re.sub(r'<ligature>(.+?)</ligature>', r'<g type="ligature">\1</g>', filedata)

filedata = re.sub(r'<\?xml version="1.0" encoding="utf-8"\?>', '', filedata)


with open('../ixml_test.xml', 'w', encoding='utf-8') as file:
    file.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/css" href="evaFontCSS.css"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>\n<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>')
    file.write(f'\n<TEI xmlns="http://www.tei-c.org/ns/1.0">')
    file.write(f"\n<teiHeader>") # Start of Header
    file.write(f"\n<fileDesc>")  # Start of fileStmt
    file.write(titleStmt)
    file.write(publicationStmt)
    file.write(f"\n<sourceDesc>")
    file.write(f"\n<msDesc>")
    file.write(msIdentifier)
    file.write(f"\n<physDesc>")
    file.write(handDesc)
    file.write(bindingDesc)
    file.write(f"\n</physDesc>")
    file.write(history)
    file.write(f"\n<msContents>")
    file.write(f"\n<summary>")
    file.write(relevant_content.strip()) # Gets Info from website ReadMe
    file.write(f"\n</summary>")
    file.write(f"\n</msContents>")
    file.write(f"\n</msDesc>")
    file.write(f"\n</sourceDesc>")
    file.write(f"\n</fileDesc>")
    file.write(f"\n<encodingDesc>")
    file.write(charDecl)
    file.write(tagsDecl)
    file.write(f"\n</encodingDesc>")
    file.write(f"\n<profileDesc>")
    file.write(langUsage)
    file.write(f"\n</profileDesc>")
    file.write(f"\n</teiHeader>")
    file.write(filedata) # Changed File
    file.write(f"\n</TEI>")

print("ixml_test complete.")