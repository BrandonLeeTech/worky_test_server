<?php
// 處理流程，包括訪問的 server 位置、判斷使用 target
require_once __DIR__ . '/includes/get_request.php';
require_once __DIR__ . '/includes/render_response.php';

$environments = [
    "local" => "http://192.168.1.111:8000/",
    "dev" => "http://127.0.0.1:8000/",
];
$api_target = $_POST['api_target'] ?? '';


$api_base = $environments["local"];
$api_url = $api_base . $api_target;

$ch = curl_init($api_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// 判斷 GET / POST
if (in_array($api_target, ['get-test'])) {
    // 只 GET，不送資料
    curl_setopt($ch, CURLOPT_HTTPGET, true);
} else {
    $data = getRequestData($api_target, $_POST);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json'
    ]);
}

$response = curl_exec($ch);
curl_close($ch);

// 呼叫統一顯示邏輯
renderResponse($response);

// 顯示 cURL 錯誤（若有）
if (curl_errno($ch)) {
    echo "<pre style='color:red;'>cURL 錯誤: " . curl_error($ch) . "</pre>";
}
?>
