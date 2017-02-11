<?php
if(isset($_POST['Enviar']))
{
    $cantidad = (int)$_POST['nvalor']; 
    echo  ' <html> ';
    echo  ' <head> ';
    echo  '        <meta charset="UTF-8"> ';
    echo  '         <title></title>     ';
    echo  '          <link href="css/form/form.css" type="text/css" rel="stylesheet"/> ';
    echo ' </head> ';
    echo ' <body> ';
    
    echo '<form method="post" action="ordenar.php" class="elegante" style="margin: auto; display: table">';
    echo ' <fieldset> ';
    echo ' <legend> Ingredso de datos </legend> ';
    
    for($i=1; $i<=$cantidad; $i++)
        {
        echo 'Valor '.$i.': <input type="text" name="matriz['.$i.']" />'."<br>\n";
        }
    echo '<input type="submit" name="Ordenar" value="Ordenar" "  />';

    echo ' <br> numero de registros <input type="text" name="cantidad" value='.$cantidad.'  >';
    
    echo ' </fieldset> ';
    echo '</form>';
         
    echo ' </body> ';
    echo ' </html> ';
}
?>
