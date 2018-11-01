<?php
$APP_ID = "your app id";
$APP_KEY = "your app key";
$IMAGE_PATH ="image path";
$queryUrl = "http://106.51.58.118:5000/get_face_vec?face_det=1";

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
$response = curl_exec($request);
echo $response;
curl_close($request);
?>
