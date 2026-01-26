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


with open('../transliterationFiles/ZL3b-n/ZL3b-n.txt', 'r', encoding='utf-8') as file:
    filedata = file.read()

replacements = {
    '<': '&lt;',
    '>': '&gt;',
    '#': '<note type="outline">',
    '@128;': '<g ref="#u20ac">€</g>',
    '@130;': '<g ref="#u201a">‚</g>',
    '@131;': '<g ref="#u0192">ƒ</g>',
    '@132;': '<g ref="#u201e">„</g>',
    '@133;': '<g ref="#u2026">…</g>',
    '@134;': '<g ref="#u2020">†</g>',
    '@135;': '<g ref="#u2021">‡</g>',
    '@136;': '<g ref="#u02c6">ˆ</g>',
    '@137;': '<g ref="#u2030">‰</g>',
    '@138;': '<g ref="#u0160">Š</g>',
    '@139;': '<g ref="#u2039">‹</g>',
    '@140;': '<g ref="#u0152">Œ</g>',
    '@142;': '<g ref="#u017d">Ž</g>',
    '@145;': '<g ref="#u2018">‘</g>',
    '@146;': '<g ref="#u2019">’</g>',
    '@147;': '<g ref="#u201c">“</g>',
    '@148;': '<g ref="#u201d">”</g>',
    '@149;': '<g ref="#u2022">•</g>',
    '@150;': '<g ref="#u2013">–</g>',
    '@151;': '<g ref="#u2014">—</g>',
    '@152;': '<g ref="#u02dc">˜</g>',
    '@153;': '<g ref="#u2122">™</g>',
    '@154;': '<g ref="#u0161">š</g>',
    '@155;': '<g ref="#u203a">›</g>',
    '@156;': '<g ref="#u0153">œ</g>',
    '@158;': '<g ref="#u017e">ž</g>',
    '@159;': '<g ref="#u0178">Ÿ</g>',
    '@160;': '<g ref="#u0020"> </g>',
    '@161;': '<g ref="#u00a1">¡</g>',
    '@162;': '<g ref="#u00a2">¢</g>',
    '@163;': '<g ref="#u00a3">£</g>',
    '@164;': '<g ref="#u00a4">¤</g>',
    '@165;': '<g ref="#u00a5">¥</g>',
    '@166;': '<g ref="#u00a6">¦</g>',
    '@167;': '<g ref="#u00a7">§</g>',
    '@168;': '<g ref="#u00a8">¨</g>',
    '@169;': '<g ref="#u00a9">©</g>',
    '@170;': '<g ref="#u00aa">ª</g>',
    '@171;': '<g ref="#u00ab">«</g>',
    '@172;': '<g ref="#u00ac">¬</g>',
    '@173;': '<g ref="#u00ad">­</g>',
    '@174;': '<g ref="#u00ae">®</g>',
    '@175;': '<g ref="#u00af">¯</g>',
    '@176;': '<g ref="#u00b0">°</g>',
    '@177;': '<g ref="#u00b1">±</g>',
    '@178;': '<g ref="#u00b2">²</g>',
    '@179;': '<g ref="#u00b3">³</g>',
    '@180;': '<g ref="#u00b4">´</g>',
    '@181;': '<g ref="#u03bc">μ</g>',
    '@182;': '<g ref="#u00b6">¶</g>',
    '@183;': '<g ref="#u00b7">·</g>',
    '@184;': '<g ref="#u00b8">¸</g>',
    '@185;': '<g ref="#u00b9">¹</g>',
    '@186;': '<g ref="#u00ba">º</g>',
    '@187;': '<g ref="#u00bb">»</g>',
    '@188;': '<g ref="#u00bc">¼</g>',
    '@189;': '<g ref="#u00bd">½</g>',
    '@190;': '<g ref="#u00be">¾</g>',
    '@191;': '<g ref="#u00bf">¿</g>',
    '@192;': '<g ref="#u00c0">À</g>',
    '@193;': '<g ref="#u00c1">Á</g>',
    '@194;': '<g ref="#u00c2">Â</g>',
    '@195;': '<g ref="#u00c3">Ã</g>',
    '@196;': '<g ref="#u00c4">Ä</g>',
    '@197;': '<g ref="#u00c5">Å</g>',
    '@198;': '<g ref="#u00c6">Æ</g>',
    '@199;': '<g ref="#u00c7">Ç</g>',
    '@200;': '<g ref="#u00c8">È</g>',
    '@201;': '<g ref="#u00c9">É</g>',
    '@202;': '<g ref="#u00ca">Ê</g>',
    '@203;': '<g ref="#u00cb">Ë</g>',
    '@204;': '<g ref="#u00cc">Ì</g>',
    '@205;': '<g ref="#u00cd">Í</g>',
    '@206;': '<g ref="#u00ce">Î</g>',
    '@207;': '<g ref="#u00cf">Ï</g>',
    '@208;': '<g ref="#u00d0">Ð</g>',
    '@209;': '<g ref="#u00d1">Ñ</g>',
    '@210;': '<g ref="#u00d2">Ò</g>',
    '@211;': '<g ref="#u00d3">Ó</g>',
    '@212;': '<g ref="#u00d4">Ô</g>',
    '@213;': '<g ref="#u00d5">Õ</g>',
    '@214;': '<g ref="#u00d6">Ö</g>',
    '@215;': '<g ref="#u00d7">×</g>',
    '@216;': '<g ref="#u00d8">Ø</g>',
    '@217;': '<g ref="#u00d9">Ù</g>',
    '@218;': '<g ref="#u00da">Ú</g>',
    '@219;': '<g ref="#u00db">Û</g>',
    '@220;': '<g ref="#u00dc">Ü</g>',
    '@221;': '<g ref="#u00dd">Ý</g>',
    '@222;': '<g ref="#u00de">Þ</g>',
    '@223;': '<g ref="#u00df">ß</g>',
    '@224;': '<g ref="#u00e0">à</g>',
    '@225;': '<g ref="#u00e1">á</g>',
    '@226;': '<g ref="#u00e2">â</g>',
    '@227;': '<g ref="#u00e3">ã</g>',
    '@228;': '<g ref="#u00e4">ä</g>',
    '@229;': '<g ref="#u00e5">å</g>',
    '@230;': '<g ref="#u00e6">æ</g>',
    '@231;': '<g ref="#u00e7">ç</g>',
    '@232;': '<g ref="#u00e8">è</g>',
    '@233;': '<g ref="#u00e9">é</g>',
    '@234;': '<g ref="#u00ea">ê</g>',
    '@235;': '<g ref="#u00eb">ë</g>',
    '@236;': '<g ref="#u00ec">ì</g>',
    '@237;': '<g ref="#u00ed">í</g>',
    '@238;': '<g ref="#u00ee">î</g>',
    '@239;': '<g ref="#u00ef">ï</g>',
    '@240;': '<g ref="#u00f0">ð</g>',
    '@241;': '<g ref="#u00f1">ñ</g>',
    '@242;': '<g ref="#u00f2">ò</g>',
    '@243;': '<g ref="#u00f3">ó</g>',
    '@244;': '<g ref="#u00f4">ô</g>',
    '@245;': '<g ref="#u00f5">õ</g>',
    '@246;': '<g ref="#u00f6">ö</g>',
    '@252;': '<g ref="#u00fc">ü</g>',
    '@253;': '<g ref="#u00fd">ý</g>',
    '@254;': '<g ref="#u00fe">þ</g>',
    '@255;': '<g ref="#u00ff">ÿ</g>',
    '&lt;!': '<note type="inline">',
    '&lt;unreadable&gt;': '<unclear/>'
}

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
filedata = re.sub(r'"\s+>', '">', filedata)
# Getting rid of first surface
filedata = filedata.replace('</surface>', '', 1)
# Getting rid of extra space in front of <note type="outline">
filedata = re.sub(r'(<note type="outline">) ', r'\1', filedata)

with open('../ZL3b-n_test1.xml', 'w', encoding='utf-8') as file:
    file.write('<?xml version="1.0" encoding="UTF-8"?><?xml-stylesheet type="text/css" href="evaFontCSS.css"?><?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?><?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>')
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
    file.write(charDecl)
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

print("ZL3b-n_test1 complete.")