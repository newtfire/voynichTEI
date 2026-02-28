<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs math"
    version="3.0">
    
   
    <xsl:variable name="titleStmt" as="element()" select="doc('../xml/header/titleStmt.xml')//titleStmt"/>
    
    <xsl:variable name="publicationStmt" as="element()" select="doc('../xml/header/publicationStmt.xml')//publicationStmt"/>
    
    <xsl:variable name="msIdentifier" as="element()" select="doc('../xml/header/msIdentifier.xml')//msIdentifier"/>
    
    <xsl:variable name="handDesc" as="element()" select="doc('../xml/header/handDesc.xml')//handDesc"/>
    
    
    <!-- ebb: KEEP GOING AND GET ALL THE PARTS OF THE TEIHEADER.  -->
 
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:output method="xml" indent="yes"/>
    
    
    <xsl:template match="*">
        <!-- Create a new element with the target namespace 'X' -->
        <xsl:element name="{local-name()}">
            <!-- Apply templates to copy attributes and child nodes -->
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="/">
        <TEI>
            <teiHeader>
               <fileDesc>
                <xsl:apply-templates select="$titleStmt"/>
                 <xsl:apply-templates select="$publicationStmt"/>
               <sourceDesc>
                <xsl:apply-templates select="$msIdentifier"/>
                <physDesc>
                    
                    <xsl:apply-templates select="$handDesc"/>
                </physDesc>
                <!-- more stuff? -->
                
            </sourceDesc>
           </fileDesc>
                
                <!-- more stuff? -->
      
            </teiHeader>
       
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
    
</xsl:stylesheet>