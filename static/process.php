<?php

if(isset($_POST['submit'])){
    $file = $_FILES['file'];
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    $fileSize = $_FILES['file']['size'];
    $fileError = $_FILES['file']['error'];

    $fileEx = explode('.', $fileName);
    $fileActualExt = strtolower(end($fileEx));

    $allowed = array('jpg','jpeg','png');
    if(in_array($fileActualExt,$allowed)){
        if($fileError === 0){
            if($fileSize < 500000){
                $fileNamNew = "you.".$fileActualExt;
                $fileDestination = 'faces/'.$fileNamNew;
                move_uploaded_file($fileTmpName,$fileDestination);
                echo "Sucess";
            }else{
                echo "The file is too big";
            }
        }else{
            echo "There was an error with uploading the file";
        }
    }else{
        echo "You cannot uplaod that extention";
    }
}?>
