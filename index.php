<?php

$flag = "/tmp/challenge/flag[a-fA-F0-9]{15}.txt";

if ( isset($_GET["dir"]) ) {
	foreach ( (new DirectoryIterator($_GET["dir"]) ) as $f ) {
		echo $f->getSize() . "\n<br>";
	}
} else {
	highlight_file(__FILE__);
}

?>
