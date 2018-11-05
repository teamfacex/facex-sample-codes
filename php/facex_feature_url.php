<?php
// you can get the app_id and app_key in user dashboard
$APP_ID = "your_app_id";
$APP_KEY = "your_app_key";
//------------------------

$IMAGE_URL = "image_url"; // add image url
$queryUrl = "http://106.51.58.118:5000/get_face_vec?face_det=1"; // feature vector url

$imageObject =  array("img" => $IMAGE_URL);
$request = curl_init();
curl_setopt($request, CURLOPT_URL, $queryUrl);
curl_setopt($request, CURLOPT_POST, true);
curl_setopt($request,CURLOPT_POSTFIELDS,$imageObject);
curl_setopt($request, CURLOPT_HTTPHEADER, array(
    "Content-type: multipart/form-data",
    "user_id:" . $APP_ID,
    "user_key:" . $APP_KEY
)
    );
curl_setopt($request, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($request); // curl response
echo $response;
curl_close($request);
?>
