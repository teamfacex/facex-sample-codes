<?php
// you can get the app_id and app_key in user dashboard
$APP_ID = "your_app_id";
$APP_KEY = "your_app_key";
//-----------------------

// add image url
$IMAGE1_URL = "first_image_url";
$IMAGE2_URL = "second_image_url";
//--------------------------

$queryUrl = "http://facexapi.com/compare_faces?face_det=1";// face compare url

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
$response = curl_exec($request); // curl response
echo $response;
curl_close($request);
?>
