<?php
$APP_ID = "your app id";
$APP_KEY = "your app key";
$IMAGE1_PATH ="first image path";
$IMAGE2_PATH ="second image path";
function makecUrlFile($file){
  $mime = mime_content_type($file);
  $info = pathinfo($file);
  $name = $info['basename'];
  $output = new CURLFile($file, $mime, $name);
  return $output;
}
$imageObject1 = makecUrlFile($IMAGE1_PATH);
$imageObject2 = makecUrlFile($IMAGE2_PATH);
$request = curl_init();
$queryUrl = "http://106.51.58.118:5000/compare_faces?face_det=1";
$imageObject =  array("img_1" => $imageObject1, "img_2" => $imageObject2);
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