<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:vn="voynich-tei"
    xmlns="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="xml" indent="yes"/>
    
    <!-- hjb: I ended up just making one teiHeader doc -->
    <xsl:variable name="teiHeader" as="element(teiHeader)" select="doc('../xml/header/teiHeader.xml')//teiHeader"/>
    <xsl:variable name="text" as="element(text)" select="doc('../xml/text/text.xml')//text"/>
    <xsl:variable name="surfaceMetadata" select="doc('../xml/surfaceMetadata/surfaceMetadata.xml')"/>
    
    <xsl:key
        name="surfaceInfoById"
        match="surfaceInfo"
        use="@xml:id"/>
    
    <!-- NAMESPACE!!! NON-TO-TEI-->
    <xsl:template match="*">
    <!-- Create a new element with the target namespace 'X' -->
    <xsl:element name="{local-name()}">
        <!-- Apply templates to copy attributes and child nodes -->
        <xsl:apply-templates select="@* | node()"/>
    </xsl:element>
    </xsl:template>

    <xsl:template match="/">
        <xsl:processing-instruction name="xml-model">
            <xsl:text>href="../odd/out/voynich-tei.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"</xsl:text>
        </xsl:processing-instruction>
        <xsl:processing-instruction name="xml-model">
            <xsl:text>href="../odd/out/voynich-tei.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"</xsl:text>
        </xsl:processing-instruction>
        <TEI>
            <xsl:apply-templates select="$teiHeader"/>
           <xsl:apply-templates/>
            <xsl:apply-templates select="$text"/>
        </TEI>
    </xsl:template>
    
    <xsl:template match="sourceDoc">
        <sourceDoc>
            <xsl:apply-templates select="* except surface"/>
            <xsl:for-each-group select="surface" group-by="quireInfo/quire">
                <surfaceGrp type="quire" n="{quireInfo/quire}">
                    <xsl:for-each-group select="current-group()" group-by="quireInfo/folio">
                        <surfaceGrp type="folio" n="{quireInfo/folio}">
                          <!--  <xsl:message select="count(current-group())"/>-->
                            <xsl:apply-templates select="current-group()"/>
                        </surfaceGrp>
                    </xsl:for-each-group>
                    
                    
                </surfaceGrp>
            </xsl:for-each-group>
        </sourceDoc>
    </xsl:template>
    
    
    <!-- 2026-05-05 We decided to add some attributes to the TEI via ODD for the surface element, 
        and then output this structure:
       
       
        <surface xml:id="..." 
          quirePage="{quirePage}"
          langCode="{language}"
          bifolio="{bifolio}"
          illus="{illus}"
          hand="{hand}"
          >

            <pb n="213" />
            TO MAKE THE PB: WE SHOULD REALLY GO BACK AND DO THIS IN IXML.
        
        </surface>
        -->
    <xsl:template match="surface">
        
        <xsl:variable name="surfaceID"
            select="(@surfaceN,@surfaceNros)[1]"/>
        
        <surface xml:id="{$surfaceID}">
            
            <!-- Copy the Voynich attributes -->
            <xsl:apply-templates select="quireInfo/*" mode="quireInfo"/>
            
            <!-- Insert graphic and zone(s) -->
            <xsl:for-each select="$surfaceMetadata/surfaceData/surfaceInfo[@id=$surfaceID]/*">
                <xsl:element name="{local-name()}" namespace="http://www.tei-c.org/ns/1.0">
                    <xsl:copy-of select="@*"/>
                </xsl:element>
            </xsl:for-each>
            
            <!-- Process the original children -->
            <xsl:apply-templates/>
            
        </surface>
        
    </xsl:template>
    
    <xsl:template match="*" mode="quireInfo">
       <xsl:attribute name="vn:{name()}"><xsl:value-of select="."/></xsl:attribute>                
    </xsl:template>
    
    <xsl:template match="firstNote">
        <note>
            <xsl:apply-templates/>
        </note>
    </xsl:template>
    
    <xsl:template match="milestone-start">
        <milestone unit="block" type="start"/>
    </xsl:template>
    
    <xsl:template match="milestone-end">
        <milestone unit="block" type="end"/>
    </xsl:template>
  
    <xsl:template match="comment">
        <note type="inline">
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
    
    <xsl:template match="figure">
        <figure type="inline">
            <xsl:apply-templates/>
        </figure>
    </xsl:template>
    
    <xsl:template match="quireInfo"/>
    
    
    <!-- WHAT IS HAPPENING WITH XML:IDs ON SURFACE ELEMENTS? -->
    <xsl:template match="@surfaceN">
        <xsl:attribute name="xml:id">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@surfaceNros">
        <xsl:attribute name="xml:id">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@lineN">
        <xsl:attribute name="n">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@lineNros">
        <xsl:attribute name="n">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@pbnum">
        <xsl:attribute name="n">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@rendition">
        <xsl:attribute name="rendition">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <!-- This can definitely be done a different way but I don't know how -->
    <xsl:template match="@xml:id">
        <xsl:attribute name="xml:id">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@hands">
        <xsl:attribute name="hands">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@notAfter">
        <xsl:attribute name="notAfter">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@notBefore">
        <xsl:attribute name="notBefore">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@when">
        <xsl:attribute name="when">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@ident">
        <xsl:attribute name="ident">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@type">
        <xsl:attribute name="type">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@target">
        <xsl:attribute name="target">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@resp">
        <xsl:attribute name="resp">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@sortKey">
        <xsl:attribute name="sortKey">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@url">
        <xsl:attribute name="url">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="@ref">
        <xsl:attribute name="ref">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <!-- -->
    
    <xsl:template match="choice">
        <xsl:choose>
            <xsl:when test="count(unclearAlt)=1">
                <xsl:apply-templates/>
            </xsl:when>
            <xsl:otherwise>
                <choice>
                    <xsl:apply-templates/>
                </choice>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>