<?php
  include('simple_html_dom.php');
  $opts = array('http'=>array('header' => "User-Agent:MyAgent/1.0\r\n"));
  $context = stream_context_create($opts);
  $header = file_get_contents('https://www.bewakoof.com/p/navy-blue-plain-full-sleeve-round-neck-men-t-shirt',false,$context);
  $html = str_get_html($header);
  echo $html->find('h1',0)->plaintext;
  echo "<br>";
  echo $html->find('span[id=testNetProdPrice]',0)->plaintext;
  echo "<br>";
  echo "<img src='";
  echo $html->find('img[title=Navy Blue Full Sleeve T-Shirt-Front Bewakoof]',0)->src;
  echo "'>";
  // foreach($html->find('img') as $element)
  //      echo $element->src . '<br>';
?>
