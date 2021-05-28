<?php
  include('simple_html_dom.php');
  $opts = array('http'=>array('header' => "User-Agent:MyAgent/1.0\r\n"));
  $context = stream_context_create($opts);
  $header = file_get_contents('https://www.amazon.in/itel-it2192-4-5cm-Heart-Black/dp/B08LJ5QYRL/ref=sr_1_1?dchild=1&keywords=B07VRZ2C4Q%7CB08LJ5T8CF%7CB083Y3QXFQ%7CB08LJ59H43%7CB08WHS2KJ8%7CB08LJ5QYRL%7CB08WHZVR5R%7CB08LJ1639J%7CB08LJ16399%7CB0859S25XY%7CB08WH9JB1V%7CB08LJ66PGF%7CB08LHX8S3W%7CB08LJ67CM2%7CB08LHX8N7X%7CB08LHX8N78%7CB08LJ5H9W8%7CB08QYP2V4G%7CB08LJ51YP4%7CB08LJ4XQ27&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=380be056-1598-4de1-8f5d-716ec5cabb30&pf_rd_r=F60B6WS356ZTW7YTK04Q&pf_rd_s=merchandised-search-9&qid=1622238305&sr=8-1',false,$context);
  $html = str_get_html($header);
  echo $html->find('h1',0)->plaintext;
  echo "<br>";
  echo $html->find('span[id=priceblock_ourprice]',0)->plaintext;
  echo "<br>";
  echo "<img src='";
  echo $html->find('img',1)->src;
  echo "'>";
  // foreach($html->find('img') as $element)
  //      echo $element->src . '<br>';
?>
