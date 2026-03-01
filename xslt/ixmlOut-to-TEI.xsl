<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs math tei"
    version="3.0">
    
    <!-- hjb: I ended up just making one teiHeader doc -->
    <xsl:variable name="teiHeader" as="element(teiHeader)" select="doc('../xml/header/teiHeader.xml')//teiHeader"/>
   
    
    <!-- ebb: KEEP GOING AND GET ALL THE PARTS OF THE TEIHEADER.  -->
 
    <xsl:mode on-no-match="shallow-copy"/>


    <xsl:template match="/">
        <TEI>
            
            <xsl:apply-templates select="$teiHeader"/>
            
       
           <xsl:apply-templates/>
     
        </TEI>
    </xsl:template>
    

    
    <xsl:template match="milestone-start">
        <milestone unit="block" type="start"/>
    </xsl:template>
    
    <xsl:template match="milestone-end">
        <milestone unit="block" type="end"/>
    </xsl:template>
  
    <xsl:template match="comment">
        <note type="outline">
            <xsl:apply-templates/>
        </note>
    </xsl:template>
    
    <xsl:template match="unclearAlt">
        <unclear>
            <xsl:apply-templates/>
        </unclear>
    </xsl:template>
    
    <xsl:template match="ligature">
        <g><xsl:apply-templates/></g>
    </xsl:template>
    
    <xsl:template match="@surfaceN">
        <xsl:attribute name="n">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@lineN">
        <xsl:attribute name="n">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    

    
    
    
</xsl:stylesheet>