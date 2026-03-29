# 🌿 Voynich TEI

A TEI analysis of the Voynich Manuscript
---
---
---
## EVA Font in Oxygen
1. Go to the repo and grab the `EVA2.tff` file and the `evaFontCSS.css` file
1. Download the RAW file for both and put them in the same repo (Or simply clone the repo)
   * ![img/evafontoxygen2.png](img/evafontoxygen2.png)
1. Click on the `eva1.tff` file and click `Install`
   * ![img/evafontoxygen3.png](img/evafontoxygen3.png)
1. Go to Oxygen and go to Options -> Preferences
   * ![img/evafontoxygen4.png](img/evafontoxygen4.png)
1. Look up `Document Type Association` and double click `TEI P5` under `Document Type`. Make sure it is enabled as well
   * ![img/evafontoxygen5.png](img/evafontoxygen5.png)
1. This step creates a new document type. Name it whatever you want. Go to the Author Tab. Then, go to the plus sign and click it
   * ![img/evafontoxygen6.png](img/evafontoxygen6.png)
1. Look for the `evaFontCSS.css` file in your documents. Title it whatever you'd like. Then click `OK`
   * ![img/evafontoxygen7.png](img/evafontoxygen7.png)
1. Click `OK`
   * ![img/evafontoxygen8.png](img/evafontoxygen8.png)
1. Click `Apply` and then `OK`
   * ![img/evafontoxygen9.png](img/evafontoxygen9.png)
1. Add `<?xml-stylesheet type="text/css" href="evaFontCSS.css"?>` to the top portion of your document like so
   * ![img/evafontoxygen11.png](img/evafontoxygen11.png)
1. You're done! Your Author Mode should now look like this, with everything within the `<line>` element now being in Voynichese and everything else in English!
   * ![img/evafontoxygen10.png](img/evafontoxygen10.png)

---

## Instructions
### Step 1: Gather Files
Clone this repo onto your computer by doing the following:
```
git clone https://github.com/newtfire/voynichTEI.git
```

### Step 2: Downloads
This is a list of programs I used in order to complete this project:
1. [OxygenXML Editor](https://www.oxygenxml.com/xml_editor/download_oxygenxml_editor.html?os=Windows)
1. [PyCharm](https://www.jetbrains.com/pycharm/?source=google&medium=cpc&campaign=amer_en_us_est_pycharm_branded&term=pycharm&content=785237935139&gad_source=1&gad_campaignid=14127625430&gclid=CjwKCAjw687NBhB4EiwAQ645dpuecQzEsyA8-SytU0ErWbuCJxzVifV3OwpJaoTVVxdhp3a2vymErRoCLCwQAvD_BwE)
1. [Markup Blitz Windows](https://github.com/newtfire/textAnalysis-Hub/blob/main/Installations/ixml-xproc-InstallNotes-Win.md#markup-blitz)
1. [Markup Blitz Mac](https://github.com/newtfire/textAnalysis-Hub/blob/main/Installations/ixml-xproc-InstallNotes-Mac.md#markup-blitz)

### Step 2.5: Python
NOTE: This step is only if you plan to use the entire ZL3b-n.txt document and not just the herbal section. If you are only using the herbal section, feel free to skip this, as the herbal.txt file already did this for you!

In PyCharm, create a VoynichTEI project, and open replaceAscii.py (Located [here](https://github.com/newtfire/voynichTEI/tree/main/python) inside the python directory).

Run the file, and you should now have a ZL3b-n_updated.txt file (Located [here](https://github.com/newtfire/voynichTEI/tree/main/ixml) inside the ixml directory).

## Step 3: Invisible XML
Go into your Bash shell and go to the VoynichTEI directory

To get an output on the entire ZL3b-n document, in your shell, type the following:
```
blitz ixml/translit.ixml transliterationFiles/ZL3b-n_updated.txt > xml/outputXML.xml
```
If you just want the herbal section instead, type the following:
```
blitz ixml/translitHerbal.ixml transliterationFiles/herbal.txt > xml/outputXMLherbal.xml
```
This sends the text documents through the invisible xml file and makes it into an XML file!

## Step 4: XSLT
Now we need to send the output XML file through an XSLT file. You will need OxygenXML to do this.

In Oxygen, open your outputXML.xml file and the ixmlOut-to-TEI.xsl document (Located [here](https://github.com/newtfire/voynichTEI/tree/main/xslt) in the xslt directory).

Switch to the XSLT Debugger Perspective, which is located at the top right of the screen:

![_src/img/methods_XSLTDebuggerPerspective.png](_src/img/methods_XSLTDebuggerPerspective.png)

In the top left corner, put `outputXML.xml` or `outputXMLherbal.xml` in the XML input, and `ixmlOut-to-TEI.xsl` in the XSL input like so:

![_src/img/methods_whatToPut.png](_src/img/methods_whatToPut.png)

When you are ready, put the filepath to where you would like your output file saved. Here, I just wrote outputTEI.xml as an example:

![_src/img/methods_output.png](_src/img/methods_output.png)

Press the run button:

![_src/img/methods_RunButton.png](_src/img/methods_RunButton.png)

Now you have it as a proper TEI file!

---

## Layout of the Manuscript
* Quire 1

![https://www.voynich.nu/q01/schema01.gif](https://www.voynich.nu/q01/schema01.gif)
* Quire 2

![https://www.voynich.nu/q02/schema02.gif](https://www.voynich.nu/q02/schema02.gif)
* Quire 3

![https://www.voynich.nu/q03/schema03.gif](https://www.voynich.nu/q03/schema03.gif)
* Quire 4

![https://www.voynich.nu/q04/schema04.gif](https://www.voynich.nu/q04/schema04.gif)
* Quire 5

![https://www.voynich.nu/q05/schema05.gif](https://www.voynich.nu/q05/schema05.gif)
* Quire 6

![https://www.voynich.nu/q06/schema06.gif](https://www.voynich.nu/q06/schema06.gif)
* Quire 7

![https://www.voynich.nu/q07/schema07.gif](https://www.voynich.nu/q07/schema07.gif)
* Quire 8

![https://www.voynich.nu/q08/schema08.gif](https://www.voynich.nu/q08/schema08.gif)
* Quire 9

![https://www.voynich.nu/q09/schema09.gif](https://www.voynich.nu/q09/schema09.gif)
* Quire 10

![https://www.voynich.nu/q10/schema10.gif](https://www.voynich.nu/q10/schema10.gif)
* Quire 11

![https://www.voynich.nu/q11/schema11.gif](https://www.voynich.nu/q11/schema11.gif)
* Quire 12

![https://www.voynich.nu/q12/schema12.gif](https://www.voynich.nu/q12/schema12.gif)
* Quire 13

![https://www.voynich.nu/q13/schema13.gif](https://www.voynich.nu/q13/schema13.gif)
* Quire 14

![https://www.voynich.nu/q14/schema14.gif](https://www.voynich.nu/q14/schema14.gif)
* Quire 15

![https://www.voynich.nu/q15/schema15.gif](https://www.voynich.nu/q15/schema15.gif)
* Quire 17

![https://www.voynich.nu/q17/schema17.gif](https://www.voynich.nu/q17/schema17.gif)
* Quire 19

![https://www.voynich.nu/q19/schema19.gif](https://www.voynich.nu/q19/schema19.gif)
* Quire 20

![https://www.voynich.nu/q20/schema20.gif](https://www.voynich.nu/q20/schema20.gif)

---

## 📄 Transliteration Files

### ZL3b-n

- The latest release of the Zandbergen-Landini transliteration of 1999 in the IVTFF 2.0 format. 
- It is a complete transliteration, including all 5389 loci that have been identified in the MS. It uses the Eva alphabet, including the high-ascii extensions.
- The file has been corrected in numerous places. Some parts of the text inside folds of the pages still need to be added.

### RF1b-e

- The first stable version of a reference transliteration, which was created automatically as a combination of the GC and ZL transliterations, in the IVTFF 2.0 format. 
- The original file was defined using the STA alphabet, and the present file is a simplification/approximation using Basic, not-capitalised Eva.

---

## 🔗 References

* Beinecke Library high-res images of the Voynich manuscript
  * [https://collections.library.yale.edu/catalog/2002046](https://collections.library.yale.edu/catalog/2002046)
* Transliteration files directory
  * [https://www.voynich.nu/data/](https://www.voynich.nu/data/)
* Layout of the Manuscript images
  * [https://www.voynich.nu/layout.html](https://www.voynich.nu/layout.html)
* Voynich Manuscript Website
  * [https://www.voynich.nu/](https://www.voynich.nu/)



