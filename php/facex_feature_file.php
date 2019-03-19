<?php
// you can get the app_id and app_key in user dashboard
$APP_ID = "your_app_id";
$APP_KEY = "your_app_key";
//------------------------

$IMAGE_PATH ="image_path"; // add image path from local system
$queryUrl = "http://facexapi.com/get_face_vec?face_det=1"; //feature vector url

function makecUrlFile($file){
  $mime = mime_content_type($file);
  $info = pathinfo($file);
  $name = $info['basename'];
  $output = new CURLFile($file, $mime, $name);
  return $output;
}


$imageObjectt = makecUrlFile($IMAGE_PATH);
$request = curl_init();
$imageObject =  array("img" => $imageObjectt);
curl_setopt($request, CURLOPT_URL, $queryUrl);
curl_setopt($request, CURLOPT_POST, true);
curl_setopt($request, CURLOPT_HTTPHEADER, array(
    "content-type: multipart/form-data",
    "user_id:" . $APP_ID,
    "user_key:" . $APP_KEY
)
    );
curl_setopt($request,CURLOPT_POSTFIELDS,$imageObject);
curl_setopt($request, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($request);// curl response
echo $response;
curl_close($request);
?>
