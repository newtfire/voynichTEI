<?xml version="1.0" encoding="UTF-8"?>
<p:declare-step name="voynich-fullText" xmlns:p="http://www.w3.org/ns/xproc"
    exclude-inline-prefixes="#all" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ex="extensions"
    xmlns:cx="http://xmlcalabash.com/ns/extensions" xmlns:c="http://www.w3.org/ns/xproc-step"
    version="3.0">

    <p:input port="source" primary="true" content-types="text/plain" href="transliterationFiles/ZL3b-n/ZL3b-n.txt"/>

      
    <p:identity message="Yo! Got a plain text input here ready to process!"/>
    
    <p:os-exec command='"C:/Program\ Files/Python313/python.exe"' args="python/replaceAscii.py"/>
    
    <p:store href="xproc/xProcOutput.xml"/>
        

</p:declare-step>