<?php
$APP_ID = "your app id";
$APP_KEY = "your app key";
$IMAGE1_URL = "first image url";
$IMAGE2_URL = "second image url";
$queryUrl = "http://106.51.58.118:5000/compare_faces?face_det=1";
$imageObject = '{"image_attr":"https://media.kairos.com/liz.jpg"}';
$imageObject =  array("img_1" => $IMAGE1_URL , "img_2" => $IMAGE2_URL);
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
$response = curl_exec($request);
echo $response;
curl_close($request);
?>
