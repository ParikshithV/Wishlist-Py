<?php
  include('simple_html_dom.php');
  $opts = array('http'=>array('header' => "User-Agent:MyAgent/1.0\r\n"));
  $context = stream_context_create($opts);
  $header = file_get_contents('https://www.bewakoof.com/p/dreamer-constellations-soft-bound-notebook',false,$context);
  $html = str_get_html($header);
  echo $html->find('h1',0)->plaintext;
  echo "<br>";
  echo $html->find('span[id=testNetProdPrice]',0)->plaintext;
  echo "<br>";
  echo "<img src='";
  echo $html->find('img',1)->src;
  echo "'>";
  // foreach($html->find('img') as $element)
  //      echo $element->src . '<br>';
?>
