---
title: Instructions
layout: base.njk
permalink: "instructions.html"
---

<header>
    <h1>{{ title }}</h1>
</header>

<div class="corpus">
    <h1>Step 1: Gather Files</h1>
    <p>Gather the files necessary for this project. To do this, clone my repo by typing the following in your terminal:</p>
    <pre><code>git clone https://github.com/newtfire/voynichTEI.git</code></pre>
</div>

<div class="corpus">
    <h1>Step 2: Downloads</h1>
    <p>This is a list of things I used in order to complete this project.</p>
    <ul>
        <li><a href="https://www.oxygenxml.com/xml_editor/download_oxygenxml_editor.html?os=Windows">OxygenXML Editor</a></li>
        <li><a href="https://github.com/newtfire/textAnalysis-Hub/blob/main/Installations/ixml-xproc-InstallNotes-Win.md">Windows Installations</a> - Scroll to Markup Blitz and download that</li>
        <li><a href="https://github.com/newtfire/textAnalysis-Hub/blob/main/Installations/ixml-xproc-InstallNotes-Mac.md">Mac Installations</a> - Scroll to Markup Blitz and download that</li>
    </ul>
</div>

<div class="corpus">
    <h1>Step 3: Python</h1>
    <p>NOTE: This step is only if you plan to use the entire ZL3b-n.txt document and not just the herbal section. If you are only using the herbal section, feel free to skip this, as the herbal.txt file already did this for you!</p>
    <p>Make sure that you can run python in your terminal.</p>
    <p>In your terminal, go into your <a href="https://github.com/newtfire/voynichTEI/tree/main/python">python</a> folder:</p>
    <pre><code>cd python</code></pre>
    <p>Run the <a href="https://github.com/newtfire/voynichTEI/tree/main/python">replaceAscii.py</a> file by typing the following:</p>
    <pre><code>python replaceAscii.py</code></pre>
    <p>You should now have <a href="https://github.com/newtfire/voynichTEI/blob/main/transliterationFiles/ZL3b-n_updated.txt">ZL3b-n_updated.txt</a> inside the <a href="https://github.com/newtfire/voynichTEI/tree/main/transliterationFiles">transliterationFiles</a> directory.</p>
</div>

<div class="corpus">
    <h1>Step 4: Invisible XML</h1>
    <p>Next we send the transliteration file through an Invisible XML grammar called <a href="https://github.com/newtfire/voynichTEI/blob/main/ixml/translit.ixml">translit.ixml</a>.</p>
    <p>To do this, in your terminal, go out of your python directory and back into the voynichTEI directory:</p>
    <pre><code>cd ..</code></pre>
    <p>Then, use Markup-Blitz to create an XML file:</p>
    <pre><code>blitz ixml/translit.ixml transliterationFiles/ZL3b-n_updated.txt > xml/outputXML.xml</code></pre>
    <p>If you just want the herbal section instead, type the following:</p>
    <pre><code>blitz ixml/translitHerbal.ixml transliterationFiles/herbal.txt > xml/outputXMLherbal.xml</code></pre>
    <p>You should now have <a href="https://github.com/newtfire/voynichTEI/blob/main/xml/outputXML.xml">outputXML.xml</a> or <a href="https://github.com/newtfire/voynichTEI/blob/main/xml/outputXMLherbal.xml">outputXMLherbal</a> in the <a href="https://github.com/newtfire/voynichTEI/tree/main/xml">xml</a> directory.</p>
</div>

<div class="corpus">
    <h1>Step 5: XSLT</h1>
    <p>Now we need to send the output XML file through an XSLT file. You will need OxygenXML to do this.</p>
    <p>In Oxygen, open your output file and <a href="https://github.com/newtfire/voynichTEI/tree/main/xslt">ixmlOut-to-TEI.xsl</a> document in the <a href="https://github.com/newtfire/voynichTEI/tree/main/xslt">xslt</a> directory.</p>
    <p>Switch to the XSLT Debugger Perspective, which is located at the top right of the screen:</p>
    <img src="img/methods_XSLTDebuggerPerspective.png">
    <p>In the top left corner, put <code>outputXML.xml</code> or <code>outputXMLherbal.xml</code> in the XML input, and <code>ixmlOut-to-TEI.xsl</code> in the XSL input like so:</p>
    <img src="img/methods_whatToPut.png">
    <p>When you are ready, put the filepath to where you would like your output file saved. In voynichTEI, this would be inside the <a href="https://github.com/newtfire/voynichTEI/tree/main/tei">tei</a> directory:</p>
    <img src="img/methods_output.png">
    <p>Press the run button:</p>
    <img src="img/methods_RunButton.png">
    <p>Now you have it as a proper TEI file!</p>
</div>