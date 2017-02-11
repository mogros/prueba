<?php
$matriz=$_REQUEST['matriz'];
$can=$_REQUEST['cantidad'];
if($_REQUEST['Ordenar'])
    {
        ///validar que no se repita el mismo numero
        for($i=1;$i<=$can;$i++){     
            $v_m1=$matriz[$i];       
            for($j=$i+1;$j<=$can;$j++){  
                $v_m2=$matriz[$j]; 
                if($v_m1==$v_m2){ 
                    printf(" <h1> ATENCION!!</h1> <br> <b> No puede ingresar el mismo numero ".$v_m1." dos veces </b>");
                    return false;
                }
            } 
         } 

         ///ordenar la matriz de menor a mayor
        for($i=1;$i<$can;$i++)
        {
          for($j=1;$j<$can;$j++){
            if($matriz[$j+1]<$matriz[$j]){
              $aux=$matriz[$j+1];
              $matriz[$j+1]=$matriz[$j];
              $matriz[$j]=$aux;
            }
           }
         }
    }
    
   printf("<br> <b> **LOS NUMEROS ORDENADOS DE FORMA ASCENDENTE**\n\n </b> <br> <br>");
   for($i=1;$i<=$can;$i++){
       if($i==$can){
            printf("[%d] ",$matriz[$i]);
       }
       else{
            printf("[%d] ,",$matriz[$i]);
       }
   }
?>