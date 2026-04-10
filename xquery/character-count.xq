declare variable $chars-by-freq := 
  let $all := string-to-codepoints(translate(/, ' ', '')) ! codepoints-to-string(.)
  let $unique := distinct-values($all)
  for $char in $unique
  let $freq := index-of($all, $char) => count()
  order by $freq
  return $char;
