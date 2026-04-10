(: Namespaces :)
declare namespace map="http://www.w3.org/2005/xpath-functions/map";

(: Variables: 
  $distinct-words: from xml document
  $scrambled-word-map: map from distinct word with alphabetized characters to original spelling(s)
    Uses: 
      $distinct-words-char-sorted: map entries from scrambled to original word(s)
  $scrambled-plant-map: map from plant with alphabetized characters to original spelling(s)
    Uses: 
      $plants: plants to find, already distinct because pulled from site map
      $scrambled-plants: map entries from plant names with letters alphabetized to original plant name(s)
:)
declare variable $distinct-words := tokenize(/) => distinct-values();
declare variable $distinct-words-char-sorted := 
  for $word in $distinct-words
  let $word-letters-sorted := string-to-codepoints($word) ! codepoints-to-string(.) => sort() => string-join()
  return map:entry($word-letters-sorted, $word);
declare variable $scrambled-word-map :=
  map:merge($distinct-words-char-sorted, map {"duplicates": "combine"});
declare variable $plants := ('bale', 'was');
declare variable $scrambled-plants :=
  for $plant in $plants
  let $plant-letters-sorted := string-to-codepoints($plant) ! codepoints-to-string(.) => sort() => string-join()
  return map:entry($plant-letters-sorted, $plant);
declare variable $scrambled-plant-map :=
  map:merge($scrambled-plants, map {"duplicates": "combine"});

(: Find words that are anagrams of plant names :)
for $plant-key in map:keys($scrambled-plant-map)
where map:contains($scrambled-word-map, $plant-key)
return $scrambled-word-map($plant-key)


  